import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from PIL import Image

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

output = Path(os.environ.get('CAPTURE_OUTPUT', '/tmp/jump-opa1-live'))
output.mkdir(parents=True, exist_ok=True)
options = Options()
options.add_argument('-headless')
device_scale = float(os.environ.get('CAPTURE_DEVICE_SCALE', '2'))
options.set_preference('layout.css.devPixelsPerPx', str(device_scale))
options.binary_location = os.environ['FIREFOX']
driver = webdriver.Firefox(service=Service(os.environ['GECKODRIVER']), options=options)
driver.set_window_size(1400, 900)
driver.set_page_load_timeout(180)
wait = WebDriverWait(driver, 180)
records = []
links = {}
capture_only = os.environ.get('CAPTURE_ONLY')
if capture_only and (output / 'provenance.json').exists():
    previous_manifest = json.loads((output / 'provenance.json').read_text())
    records = previous_manifest['screenshots']
    links = previous_manifest['links']


def table_url(kind, filters, sort='rowid', descending=False):
    names = {'crispr_feature': 'crispr_interpretable_features', 'orf_feature': 'orf_interpretable_features', 'crispr_matches': 'crispr', 'crispr_gallery': 'crispr_gallery'}
    base = 'https://lite.datasette.io/?metadata=https://raw.githubusercontent.com/broadinstitute/monorepo/main/libs/jump_rr/metadata/' + kind + '.json&install=datasette-json-html&parquet=https://d3dw4c1b79pj57.cloudfront.net/latest/' + names[kind] + '.parquet/content'
    params = {}
    for column, operator, value in filters:
        params[column + '__' + operator] = value
    params['_sort_desc' if descending else '_sort'] = sort
    if kind == 'crispr_gallery':
        params['_col'] = ['Perturbation', 'JCP2022', 'Site 0', 'Source', 'Plate', 'Well']
    return base + '#/data/content?' + urlencode(params, doseq=True)


def load(url):
    if driver.current_url != url:
        previous = driver.find_elements(By.CSS_SELECTOR, 'table.rows-and-columns')
        driver.get(url)
        if previous:
            wait.until(expected_conditions.staleness_of(previous[0]))
    wait.until(lambda browser: browser.find_elements(By.CSS_SELECTOR, 'table.rows-and-columns tbody tr'))
    wait.until(lambda browser: 'OPA1' in browser.find_element(By.CSS_SELECTOR, 'table.rows-and-columns').text)
    driver.execute_script("document.documentElement.style.zoom='1.25'; document.querySelectorAll('[style]').forEach(e=>{e.style.outline='';e.style.outlineOffset=''})")
    driver.execute_script('window.scrollTo(0,0)')
    driver.execute_script('document.querySelectorAll("*").forEach(element=>{if(element.scrollLeft)element.scrollLeft=0})')
    return driver.find_element(By.CSS_SELECTOR, 'table.rows-and-columns')


def form():
    return driver.find_element(By.NAME, '_filter_column').find_element(By.XPATH, 'ancestor::form')


def capture(name, anchor=None, columns=(), focus=None):
    if capture_only and name not in capture_only.split(','):
        return
    driver.execute_script('if(document.activeElement instanceof HTMLElement) document.activeElement.blur()')
    if anchor is not None:
        driver.execute_script('window.scrollTo(0, Math.max(0, arguments[0].getBoundingClientRect().top+window.scrollY-40))', anchor)
    if focus:
        for header in driver.find_elements(By.CSS_SELECTOR, 'table.rows-and-columns th'):
            if header.text.strip() == focus:
                driver.execute_script('let target=arguments[0]; for(let parent=target.parentElement;parent;parent=parent.parentElement){if(parent.scrollWidth>parent.clientWidth+20){parent.scrollLeft+=Math.max(0,target.getBoundingClientRect().left-parent.getBoundingClientRect().left-30)/1.25;break}}', header)
    driver.execute_async_script('const done=arguments[arguments.length-1]; const images=[...document.images].filter(i=>{const r=i.getBoundingClientRect();return r.top<innerHeight && r.bottom>0}); Promise.all(images.map(i=>i.complete?Promise.resolve():new Promise(r=>{i.onload=r;i.onerror=r;setTimeout(r,15000)}))).then(()=>setTimeout(done,500));')
    path = output / name
    if name == '01-availability.png':
        driver.find_element(By.CSS_SELECTOR, '.dt-container').screenshot(str(path))
    else:
        driver.save_screenshot(str(path))
    # Preserve every captured pixel; density metadata keeps the existing TeX
    # crops at their original physical size with a 2x-resolution screenshot.
    with Image.open(path) as screenshot:
        screenshot.save(path, dpi=(72 * device_scale, 72 * device_scale))
    image_sources = driver.execute_script('return [...document.images].filter(i=>i.getBoundingClientRect().bottom>0 && i.getBoundingClientRect().top<innerHeight).map(i=>({src:i.currentSrc,width:i.naturalWidth,height:i.naturalHeight,display_width:i.getBoundingClientRect().width,display_height:i.getBoundingClientRect().height,loaded:i.complete && i.naturalWidth>0}))')
    records[:] = [record for record in records if record['path'] != 'assets/opa1-tutorial-screenshots/' + name]
    records.append({'path': 'assets/opa1-tutorial-screenshots/' + name, 'url': driver.current_url, 'sha256': hashlib.sha256(path.read_bytes()).hexdigest(), 'scroll': driver.execute_script('return [scrollX,scrollY]'), 'highlighted_columns': [], 'title': driver.title, 'viewport': driver.execute_script('return [innerWidth,innerHeight]'), 'page_zoom': 1.25, 'device_pixel_ratio': driver.execute_script('return devicePixelRatio'), 'image_sources': image_sources})
    print('CAPTURED', name, driver.title, flush=True)
    if capture_only and name == capture_only.split(',')[-1]:
        raise SystemExit(0)


try:
    driver.set_window_size(1250, 850)
    availability = 'https://broadinstitute.github.io/jump_hub/reference/00_gene_index.html'
    driver.get(availability)
    search = wait.until(lambda browser: browser.find_element(By.CSS_SELECTOR, 'input[type=search]'))
    search.send_keys('OPA')
    wait.until(lambda browser: 'OPALIN' in browser.find_element(By.CSS_SELECTOR, 'table').text and 'A1BG' not in browser.find_element(By.CSS_SELECTOR, 'table').text)
    driver.execute_script("document.documentElement.style.zoom='1.25'")
    capture('01-availability.png', search)
    links['Available genes (search OPA)'] = availability

    exact = [('Perturbation', 'exact', 'OPA1')]
    driver.set_window_size(1400, 900)
    crispr_url = table_url('crispr_feature', exact, 'Feature Rank')
    load(crispr_url)
    links['OPA1 CRISPR features'] = crispr_url
    capture('02-columns.png')
    capture('03-filters.png', form())
    load(crispr_url)
    capture('08-crispr-features.png', form(), ('Feature', 'Channel', "Cohen's d", 'Feature significance'))
    load(crispr_url)
    capture('06-activity.png', form(), ('Perturbation', 'Corrected p-value', 'Phenotypic activity'), 'Perturbation')
    load(crispr_url)
    capture('07-feature-row.png', driver.find_element(By.CSS_SELECTOR, 'table.rows-and-columns'), ('Compartment', 'Feature', 'Channel', "Cohen's d"))
    export_url = table_url('crispr_feature', exact + [('Compartment', 'in', 'Cytoplasm,Nuclei')], 'Feature Rank')
    load(export_url)
    links['OPA1 filtered export'] = export_url
    capture('11-export.png', form())

    orf_url = table_url('orf_feature', exact, 'Feature Rank')
    load(orf_url)
    links['OPA1 ORF features'] = orf_url
    capture('09-orf-features.png', form(), ('Feature', 'Channel', 'Corrected p-value', 'Phenotypic activity'))

    matches_url = table_url('crispr_matches', exact, 'Perturbation-Match Similarity', True)
    load(matches_url)
    links['OPA1 CRISPR matches'] = matches_url
    capture('10-matches.png', form(), ('Match', 'Perturbation-Match Similarity'))

    gallery_url = table_url('crispr_gallery', exact + [('Plate', 'exact', 'CP-CC9-R1-06')])
    load(gallery_url)
    links['OPA1 gallery'] = gallery_url
    capture('04-gallery-perturbation.png', form(), ('Perturbation', 'Plate', 'Well'))
    controls_url = table_url('crispr_gallery', [('Perturbation', 'in', 'OPA1,no-guide,non-targeting'), ('Plate', 'exact', 'CP-CC9-R1-06')], 'Perturbation')
    load(controls_url)
    links['OPA1 with plate-matched controls'] = controls_url
    capture('05-gallery-controls.png', form(), ('Perturbation', 'Plate', 'Well'))
finally:
    (output / 'provenance.json').write_text(json.dumps({'captured_at': datetime.now(timezone.utc).isoformat(), 'method': 'Actual Firefox screenshots of public JUMP Hub and Datasette Lite interfaces; 125% page zoom, high-density browser rendering (per-image device_pixel_ratio), lossless PNG and native column selection; no red or blue callout boxes, reconstructed UI, post-capture resizing or synthetic cell detail. PNG density preserves existing slide crops.', 'browser': driver.capabilities.get('browserVersion'), 'screenshots': records, 'links': links}, indent=2) + '\n')
    driver.quit()
