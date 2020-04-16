import os
from gimpfu import *
import array
import numpy as np

def myplugin(img,layer):



 

# the procedure code starts here

white=(255, 255, 255)
black=(0,0,0)
img=gimp.image_list()[0]
print img
layer = pdb.gimp_image_get_active_layer(img)
highlights = pdb.gimp_histogram(layer, 0, 179, 255)
layer_copy=img.layers[0].copy()
reg_layer_A=layer_copy.get_pixel_rgn(0,0,img.width,img.height,False,False) #prendo la regione che mi interessa da layer che ho copiato prima


src_pixels_reg_A=array.array("B",reg_layer_A[0:img.width,0:img.height])# prendo i singoli valori dei pixel


valori_normalizzati=_create_normalized_frequencies_greyscale(src_pixels_reg_A) #normalizzao i singoli valori dei pixel
img.add_layer(layer_copy,3) #add layer in gimp posizione 3

    # the procedure code ends here

def prova():
    img=gimp.image_list()[0]
    
    layer = pdb.gimp_image_get_active_layer(img)
    layer_copy=img.layers[0].copy()
    print(img.layers)
    array_temp=[]#qui ho i valori che devo normalizzare
    for i in range(0,256):
        highlights = pdb.gimp_histogram(layer, 0, i, i)
        array_temp.append(highlights[4])
        #print(highlights[4])
        
    massimo=max(array_temp)
    #indice_massimo=array_temp.index(max(array_temp))
   
    minimo=min(array_temp)
    #indice_minimo=array_temp.index(min(array_temp))
    
    array_normalizzato=[]#qui ho i valori che sono normalizzati
    L=[255 / (massimo - minimo)]
    print(L)
    for x in range(layer.width):
        for y in range(layer.height):
            r=layer_copy.get_pixel(x, y)[0]
            print(r)
            t=r#qui praticamente devo applicare la formula per normalizzare
            ta=int(t)-int(minimo)
            #te=float(int(ta))*L
            te=ta*255
            ti=te/(massimo-minimo)
            finale=int(ti)
            print(finale)
            layer_copy.set_pixel(x, y, (abs(finale),))
            #layer.set_pixel(x, y, (t, L))
            #layer_copy.set_pixel(x,y,(finale,0,0))
    #layer.update()
    pdb.gimp_drawable_update(layer_copy, x, y, layer.width, layer.height)
    img.add_layer(layer_copy,3)


def controlla(array_passato):
    for f in array_passato:
        print(f)
        print("ok")
     

register(
         "python-fu-myplugin",
         N_("A short piece of information about the procedure."),
         "More detailed information about the procedure.",
         "The author of the procedure.",
         "The copyright holder for the procedure (usually the same as the author).",
         "The date when the procedure was written.",
         N_("_My plug in"),
         "GRAY*",
         [
          (PF_IMAGE, "image",       "Input GRAYSCALE image", None),
          (PF_DRAWABLE, "drawable", "Input drawable", None),
          ],
         [],
         myplugin,
         menu="<Image>/Filters/My plug in menu",
         domain=("gimp20-python", gimp.locale_directory)
         )
main()
