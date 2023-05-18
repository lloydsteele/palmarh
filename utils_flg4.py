import seaborn as sns
from skimage import io
from skimage.filters import sato
import os
import seaborn as sns
from skimage.transform import resize
import glob
import math
from scipy.stats import mannwhitneyu, f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from matplotlib import pyplot as plt
import matplotlib
import numpy as np


"""
Function for p-values using one-way ANOVA and Tukey correction
"""
def oneway_anova_and_tukey_pvalues(a, b, c):
    F, p = f_oneway(a, b, c)
    print('Statistics=%.3f, p=%.3f' % (F, p))
    scores = a + b + c
    group = []
    for i in range(len(a)):
        group.append('WT')
    for i in range(len(b)):
        group.append('Het')
    for i in range(len(c)):
        group.append('Hom')
    df = pd.DataFrame({'score': scores, 'group': group})
    tukey = pairwise_tukeyhsd(endog=df['score'],
                             groups=df['group'],
                             alpha=0.05)
    print(tukey)  

            


"""
Functions for plotting boxplot and adding statistical annotation
"""
def plotbox7(a, xa, ya, ylabel, colours=[], alpha=0.5, s=3.5, altlabel=False ):
    sns.set(style="white")
    boxplot_width = 0.1   
    if colours == 'regular':
        colours=['lightskyblue','coral', 'dimgrey']
        ax = sns.swarmplot(x=xa, y=ya, data=a, palette=colours, alpha=alpha, s=s)
    elif colours == 'alternative':
        colours="ch:s=.25,rot=-.25"
        ax = sns.swarmplot(x=xa, y=ya, data=a, palette=colours, alpha=alpha, s=s)  
    elif colours:
        try:
            ax = sns.swarmplot(x=xa, y=ya, data=a, palette=colours, alpha=alpha, s=s)
        except:
            ax = sns.swarmplot(x=xa, y=ya, data=a, alpha=alpha, s=s)
    else:
        ax = sns.swarmplot(x=xa, y=ya, data=a, palette=colours, alpha=alpha, s=s)
    sns.boxplot(x=xa, y=ya, data=a, width=boxplot_width, ax=ax, 
                boxprops={'facecolor':'None'})
    if  not altlabel:
        plt.xticks([0, 1, 2], ['Wild Type', 'Heterozygous', 'Homozygous or\ncompound het'])
    else:
        plt.xticks([0, 1, 2], ["Wild Type\n(n=324)", "Heterozygous\n(n=179)", "Homozygous or compound\nhet. (n=28)"])
    ax.set_xlabel('Filaggrin gene mutation status', fontsize=14)
    ax.set_ylabel(ylabel, fontsize=14)
    ax.yaxis.set_major_formatter(matplotlib.ticker.StrMethodFormatter('{x:,.0f}'))


def addstats(result01, result12, result02, a, ya):
    x1, x2 = 0, 1   # columns 'Sat' and 'Sun' (first column: 0, see plt.xticks())
    y = a[ya].max() + (a[ya].max() * 0.05 )
    h = 2
    col = 'k'

    plt.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=1.5, c=col)
    plt.text((x1+x2)*.5, y+h, result01, ha='center', va='bottom', color=col)
    ###COMPARISON 1 AND 2
    x1, x2 = 1, 2  

    y = a[ya].max() + (a[ya].max() * 0.1 )
    plt.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=1.5, c=col)
    plt.text((x1+x2)*.5, y+h, result12, ha='center', va='bottom', color=col)

    ###COMPARISON 0 AND 1
    x1, x2 = 0, 2    

    y = a[ya].max() + (a[ya].max() * 0.18 )

    plt.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=1.5, c=col)
    plt.text((x1+x2)*.5, y+h, result02, ha='center', va='bottom', color=col)
    
"""
v8 limits y-axis to 50 000
"""

def plotbox8(a, xa, ya, ylabel, colours=[], alpha=0.5, s=3.5, altlabel=False ):
    sns.set(style="white")
    boxplot_width = 0.1   
    if colours == 'regular':
        colours=['lightskyblue','coral', 'dimgrey']
        ax = sns.swarmplot(x=xa, y=ya, data=a, palette=colours, alpha=alpha, s=s)
    elif colours == 'alternative':
        colours="ch:s=.25,rot=-.25"
        ax = sns.swarmplot(x=xa, y=ya, data=a, palette=colours, alpha=alpha, s=s)  
    elif colours:
        try:
            ax = sns.swarmplot(x=xa, y=ya, data=a, palette=colours, alpha=alpha, s=s)
        except:
            ax = sns.swarmplot(x=xa, y=ya, data=a, alpha=alpha, s=s)
    else:
        ax = sns.swarmplot(x=xa, y=ya, data=a, palette=colours, alpha=alpha, s=s)
    sns.boxplot(x=xa, y=ya, data=a, width=boxplot_width, ax=ax, 
                boxprops={'facecolor':'None'})
    if  not altlabel:
        plt.xticks([0, 1, 2], ['Wild Type', 'Heterozygous', 'Homozygous or\ncompound het'])
    else:
        plt.xticks([0, 1, 2], ["Wild Type\n(n=324)", "Heterozygous\n(n=179)", "Homozygous or compound\nhet. (n=28)"])
    ax.set_ylim(0, 50000)
    ax.set_xlabel('Filaggrin gene mutation status', fontsize=14)
    ax.set_ylabel(ylabel, fontsize=14)
    ax.yaxis.set_major_formatter(matplotlib.ticker.StrMethodFormatter('{x:,.0f}'))

 

def pvalues(a, b, c):
    F, p = f_oneway(a, b, c)
    print('Statistics=%.3f, p=%.3f' % (F, p))
    scores = a + b + c
    group = []
    for i in range(len(a)):
        group.append('WT')
    for i in range(len(b)):
        group.append('Het')
    for i in range(len(c)):
        group.append('Homo')
    df = pd.DataFrame({'score': scores, 'group': group})
    tukey = pairwise_tukeyhsd(endog=df['score'],
                             groups=df['group'],
                             alpha=0.05)
    print(tukey)  




def plotbox(a, xa, ya, ylabel, alpha=0.5, s=3.5):
    """
    Generate a combined boxplot and swarmplot using seaborn and matplotlib.

    This function first plots a swarmplot based on the provided data and then overlays
    a boxplot on top of it. The swarmplot points are shifted slightly for visibility.
    The boxplot width is also adjusted for aesthetic reasons. The x-axis labels are
    set to specific categories of gene mutation status.

    Args:
    a (DataFrame): The data to plot. Must contain at least two columns, specified by xa and ya.
    xa (str): The name of the column in 'a' to use for the x-axis.
    ya (str): The name of the column in 'a' to use for the y-axis.
    ylabel (str): The label to use for the y-axis.
    alpha (float, optional): The transparency of the points in the swarmplot. Defaults to 0.5.
    s (float, optional): The size of the points in the swarmplot. Defaults to 3.5.

    Returns:
    None. This function plots the figure but does not return it.
    """
        
    sns.set(style="white")
    boxplot_width = 0.1  
    swarmplot_offset = -0.5 
    xlim_offset = -1  
    colours = ['lightskyblue','coral', 'dimgrey']
    ax = sns.swarmplot(x=xa, y=ya, data=a, palette=colours, alpha=alpha, s=s)
    path_collections = [child for child in ax.get_children() 
                        if isinstance(child,matplotlib.collections.PathCollection)] 
    for path_collection in path_collections: 
        x,y = np.array(path_collection.get_offsets()).T 
        xnew = x + swarmplot_offset
        offsets = list(zip(xnew,y)) 
        path_collection.set_offsets(offsets)
    sns.boxplot(x=xa, y=ya, data=a, width=boxplot_width, ax=ax, palette=colours) 
    def change_width(ax, new_value):
        for patch in ax.patches:
            current_width = patch.get_width()
            diff = current_width - new_value
            # change patch width
            patch.set_width(new_value)
            # re-center patch
            patch.set_x(patch.get_x() + diff * .5)
    change_width(ax,.25)
    plt.xticks([0, 1.1, 2.3], ['Wild Type', 'Heterozygous', 'Homozygous or \ncompound het'])
    ax.set_xticklabels(ax.get_xticklabels(), ha="right")  
    ax.set_xlim(xlim_offset,ax.get_xlim()[1]) 
    ax.set_xlabel('Filaggrin gene mutation status', fontsize=14)
    ax.set_ylabel(ylabel, fontsize=14)
    ax.yaxis.set_major_formatter(matplotlib.ticker.StrMethodFormatter('{x:,.0f}'))



def count_images(path):
    """
    Counts the number of images in a specified directory.

    This function iterates over all files in the given directory,
    and counts the ones with image file extensions (.png, .jpg, .jpeg, .gif),
    excluding files that start with a '.'.

    Args:
    path (str): The directory path where to count image files.

    Returns:
    int: The number of image files in the directory.
    """
    
    image_count = sum(fname.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')) and not fname.startswith('.') for fname in os.listdir(path))
    print(f"Image count for {path}: {image_count}")
    return image_count


def extract_hyperlinearity(path, store, threshold=0.02):
    """
    Extracts hyperlinearity scores into a provided dictionary.
    
    This function navigates through a directory of images, resizes them, applies 
    the Sato filter for ridge detection, and computes a hyperlinearity score for each.
    This score is the count of pixels with a value above a specified threshold. The scores 
    are stored in the passed dictionary where the key is the image name and the value is the score.

    Args:
        path (str): The directory path where the images are located.
        store (dict): The dictionary where the image names and corresponding scores will be stored.
        threshold (float, optional): The cutoff value for the hyperlinearity score calculation.
            Defaults to 0.02.

    Returns:
        None. The function directly modifies the passed 'store' dictionary.
    """
    length = len(os.listdir(path))
    i=0 
    for image_path in os.listdir(path):
        if not image_path.startswith('.'):
            i = i+1
            print(f"{i} of {length-1}") #path: {path}, type: {store}")
            input_path = os.path.join(path, image_path)
            img = io.imread(input_path, as_gray=True)
            img = resize(img, (512, 256))
            imagewt = sato(img, mode='constant')
            number = np.sum(imagewt>threshold)
            name = image_path
            store[name] = number