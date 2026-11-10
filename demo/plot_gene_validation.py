# /// script
# dependencies = ["matplotlib==3.10.8", "numpy==2.4.2"]
# ///
"""Vector slide figure from the measured OPA1/DNM1L analysis, not a UI mockup."""
import csv
import json
from pathlib import Path
import subprocess
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'demo/opa1-dnm1l-analysis'
OUT = ROOT / 'assets/opa1-dnm1l-analysis'
try:
    font = subprocess.check_output(['kpsewhich','FiraSans-Regular.otf'],text=True).strip()
    font_manager.fontManager.addfont(font)
    family = font_manager.FontProperties(fname=font).get_name()
except (OSError, subprocess.CalledProcessError):
    family = 'DejaVu Sans'
plt.rcParams.update({'font.family':family,'font.size':16,'axes.titlesize':19,'axes.labelsize':16,'xtick.labelsize':15,'ytick.labelsize':16,'pdf.fonttype':3,'axes.spines.top':False,'axes.spines.right':False,'axes.edgecolor':'#80898b','text.color':'#22373b','axes.labelcolor':'#22373b'})
with (DATA/'all-features.csv').open() as f:
    rows=list(csv.DictReader(f))
with (DATA/'representative-feature-wells.csv').open() as f:
    wells=list(csv.DictReader(f))
x=np.array([float(r['OPA1_d']) for r in rows])
y=np.array([float(r['DNM1L_d']) for r in rows])
selected=np.array([r['opposite']=='true' and r['both_q05']=='true' for r in rows])
assert len(rows)==3651 and selected.sum()==15 and (x*y>0).sum()==3154
fig=plt.figure(figsize=(13.5,4.4),facecolor='white')
gs=fig.add_gridspec(2,2,width_ratios=[1,1.45],wspace=.54,hspace=.75,left=.075,right=.925,bottom=.14,top=.86)
ax=fig.add_subplot(gs[:,0])
ax.axhline(0,color='#aab1b2',lw=.8,zorder=0)
ax.axvline(0,color='#aab1b2',lw=.8,zorder=0)
ax.scatter(x[~selected],y[~selected],s=9,c='#a5adb0',alpha=.42,linewidths=0)
ax.scatter(x[selected],y[selected],s=27,c='#c16e19',linewidths=.4,edgecolors='white',zorder=3)
ax.set(xlim=(-6.5,6.5),ylim=(-6.5,6.5),xticks=[-6,-3,0,3,6],yticks=[-6,-3,0,3,6],xlabel='OPA1 effect (Cohen’s d)',ylabel='DNM1L effect (Cohen’s d)')
ax.set_title('All 3,651 feature shifts',loc='left',pad=17)
ax.text(.02,1.015,'86.4% same direction',transform=ax.transAxes,fontsize=16)
ax.text(.04,.04,'15 opposing mitochondrial features',transform=ax.transAxes,color='#a45409',fontsize=14)

features=[('Nuclei_ObjectSkeleton_NumberTrunks_mito_skel','Mitochondrial skeleton trunks'),('Cells_RadialDistribution_RadialCV_mito_tubeness_15of16','Mito tubeness variation · radial bin 15/16')]
groups=[('OPA1 KO','#17817c'),('OPA1 controls','#8a9294'),('DNM1L controls','#8a9294'),('DNM1L KO','#8155a6')]
for k,(feature,title) in enumerate(features):
    ax=fig.add_subplot(gs[k,1])
    values=[np.array([float(r['value']) for r in wells if r['feature']==feature and r['group']==name]) for name,_ in groups]
    assert [len(v) for v in values]==[5,101,125,6]
    means=[v.mean() for v in values]
    assert all(min(means[0],means[3])<v<max(means[0],means[3]) for v in means[1:3])
    for i,((name,color),vals) in enumerate(zip(groups,values)):
        jitter=((np.arange(len(vals))*7)%13-6)*.022
        ax.scatter(vals,3-i+jitter,s=14 if 'KO' in name else 7,c=color,alpha=.8 if 'KO' in name else .3,linewidths=0)
        ax.scatter([vals.mean()],[3-i],marker='D',s=64,c=color,edgecolors='white',linewidths=.9,zorder=4)
        ax.text(1.015,3-i,f'{vals.mean():+.2f}',transform=ax.get_yaxis_transform(),va='center',fontsize=16,color=color)
    ax.set(yticks=[3,2,1,0],yticklabels=[g[0] for g in groups],ylim=(-.55,3.55),xlim=(-8.4,6),xticks=[-8,-4,0,4])
    ax.set_title(title,loc='left',pad=10)
    ax.spines['left'].set_visible(False)
    ax.tick_params(axis='y',length=0)
    if k==1:
        ax.set_xlabel('Normalized feature value · before control subtraction',fontsize=14)
fig.savefig(OUT/'feature-validation.pdf',metadata={'Title':'OPA1 and DNM1L feature shifts and plate-matched controls','CreationDate':None,'ModDate':None})
fig.savefig(OUT/'feature-validation.png',dpi=180)
print(OUT/'feature-validation.pdf')
