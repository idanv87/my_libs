import numpy as np
import matplotlib.pyplot as plt

def plot_axis(ax,x,y, **kwargs):

    d=kwargs
    try:
        ax.plot(x,y, color=d['color'],  label=d['label'], linestyle=d['line_style'])
        ax.legend()
    except:    
         ax.plot(x,y, color=d['color'])
    try:     
        ax.set_title(d['title'])
    except:
         pass    
    try:
        ax.set_xlabel(d['xlabel'])
        ax.set_ylabel(d['ylabel']) 
    except:
         pass    
    # f'err={y[-1]:.2e}'
    try:
        ax.text(d['x_text'], d['y_text'], d['text'], c=d['color'])
    except:
        pass  

def plot_arrow(ax, **kwargs):
        d=kwargs
        ax.annotate('',
                xy = d['end'],
                xytext =d['start'],
                arrowprops = dict(facecolor = 'black', width = 0.2, headwidth = 8),
                horizontalalignment = 'center') 


def save_eps(path):
        plt.savefig(path, format='eps',bbox_inches='tight')
        plt.show(block=False)


 