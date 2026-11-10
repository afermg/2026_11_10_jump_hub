"""Capture the actual nine-site CRISPR Gallery on the MBP, not a one-site row."""
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait

BASE = 'https://lite.datasette.io/?metadata=https://raw.githubusercontent.com/broadinstitute/monorepo/main/libs/jump_rr/metadata/crispr_gallery.json&install=datasette-json-html&parquet=https://d3dw4c1b79pj57.cloudfront.net/latest/crispr_gallery.parquet/content'
columns = ['Perturbation','Plate','Well'] + [f'Site {i}' for i in range(9)]
url = BASE + '#/data/content?' + urlencode({'Perturbation__exact':'OPA1','_col':columns},doseq=True)
out = Path(os.environ.get('CAPTURE_OUTPUT','/tmp/opa1-full-gallery'))
out.mkdir(parents=True,exist_ok=True)
options=Options()
options.add_argument('-headless')
options.binary_location=os.environ['FIREFOX']
options.set_preference('layout.css.devPixelsPerPx','6')
driver=webdriver.Firefox(service=Service(os.environ['GECKODRIVER']),options=options)
try:
    driver.set_window_size(1700,1200)
    driver.set_page_load_timeout(180)
    driver.get(url)
    wait=WebDriverWait(driver,180)
    wait.until(lambda d:len(d.find_elements(By.CSS_SELECTOR,'table.rows-and-columns tbody tr'))==5)
    table=driver.find_element(By.CSS_SELECTOR,'table.rows-and-columns')
    assert 'OPA1' in table.text
    assert driver.find_element(By.TAG_NAME,'h1').text == 'CRISPR Gallery'
    wait.until(lambda d:len(d.find_elements(By.CSS_SELECTOR,'table.rows-and-columns img'))==45)
    driver.set_script_timeout(60)
    driver.execute_async_script('const done=arguments[arguments.length-1]; Promise.all([...document.querySelectorAll("table.rows-and-columns img")].map(i=>i.complete?Promise.resolve():new Promise(r=>{i.onload=r;i.onerror=r;setTimeout(r,25000)}))).then(done)')
    images=driver.execute_script('return [...document.querySelectorAll("table.rows-and-columns img")].map(i=>({src:i.currentSrc,width:i.naturalWidth,height:i.naturalHeight,display_width:i.getBoundingClientRect().width,display_height:i.getBoundingClientRect().height,loaded:i.complete&&i.naturalWidth>0}))')
    assert all(i['loaded'] and i['width']==1280 and i['height']==1080 for i in images)
    path=out/'00-opa1-crispr-gallery.png'
    table.screenshot(str(path))
    provenance={'captured_at':datetime.now(timezone.utc).isoformat(),'url':driver.current_url,'user_supplied_base':BASE+'#/data/content','title':driver.find_element(By.TAG_NAME,'h1').text,'method':'Actual Firefox table-element screenshot. Only native gene filter and native column selection; all nine site columns and all five OPA1 wells. No plate filter, CSS rewriting, synthetic content, callouts, image resizing or sharpening. Source JPEGs are 1280x1080. Browser rendering at DPR 6.','path':'assets/opa1-tutorial-screenshots/00-opa1-crispr-gallery.png','sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'browser':driver.capabilities['browserVersion'],'device_pixel_ratio':driver.execute_script('return devicePixelRatio'),'headers':[e.text for e in table.find_elements(By.TAG_NAME,'th')],'rows':5,'images':images}
    (out/'provenance.json').write_text(json.dumps(provenance,indent=2)+'\n')
    print(json.dumps({k:v for k,v in provenance.items() if k!='images'}),flush=True)
finally:
    driver.quit()
