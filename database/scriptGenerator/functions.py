import os.path

def pathToFile(idDex):
    id = ""
    if(len(str(idDex))==1):
        id = "000"+str(idDex)
    if(len(str(idDex))==2):
        id = "00"+str(idDex)
    if(len(str(idDex))==3):
        id = "0"+str(idDex)
    pathToSprite="poke_capture_0000_000_uk_n_00000000_f_n.png"
    if(os.path.isfile("../../home_sprites/poke_capture_"+id+"_000_"+"mf_n_00000000_f_n.png")):
        pathToSprite = "poke_capture_"+id+"_000_"+"mf_n_00000000_f_"
    if(os.path.isfile("../../home_sprites/poke_capture_"+id+"_000_"+"fd_n_00000000_f_n.png")):
        pathToSprite = "poke_capture_"+id+"_000_"+"fd_n_00000000_f_"
    if(os.path.isfile("../../home_sprites/poke_capture_"+id+"_000_"+"mo_n_00000000_f_n.png")):
        pathToSprite = "poke_capture_"+id+"_000_"+"mo_n_00000000_f_"
    if(os.path.isfile("../../home_sprites/poke_capture_"+id+"_000_"+"fo_n_00000000_f_n.png")):
        pathToSprite = "poke_capture_"+id+"_000_"+"fo_n_00000000_f_"
    if(os.path.isfile("../../home_sprites/poke_capture_"+id+"_000_"+"uk_n_00000000_f_n.png")):
        pathToSprite = "poke_capture_"+id+"_000_"+"uk_n_00000000_f_"
    return pathToSprite
