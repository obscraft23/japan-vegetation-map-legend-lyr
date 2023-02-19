# auther: obscraft23 https://github.com/obscraft23
# last update: 2023-02-19
# tested on Google Colaboratory

import zipfile
from tqdm import tqdm
import os
import pathlib

res =[]

with zipfile.ZipFile("vg67.zip", 'r') as zf:
  filelist = zf.namelist()

  for i in range(len(filelist)):
    print(i,end="")
    
    with zf.open(filelist[i], 'r') as zf_0:
      with zipfile.ZipFile(zf_0, 'r') as shp:
        shplist = shp.namelist()

        for ii in (range(len(shplist))):
          with shp.open( shplist[ii], 'r') as shp_0:
            with zipfile.ZipFile(shp_0, 'r') as temp:
              tmp = [tt for tt in temp.namelist() if ".lyr" in tt]
              if len(tmp) > 0:
                legendfname = tmp[0].encode("cp437").decode("cp932", errors="ignore")

                if not (legendfname in res):
                  res.append(legendfname)
                  with temp.open(tmp[0],"r") as lyr:
                    contents = lyr.read()
                    fname = os.path.basename(legendfname)
                    f = open(fname,"wb")
                    f.write(contents)
                    f.close()