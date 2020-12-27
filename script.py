import rasterio
from rasterio.merge import merge

from pathlib import Path

SRC_FOLDER = 'source_images_oza'
OUT_FOLDER = 'mosaic_images_oza'

src_images = [rasterio.open(path)
              for path in (Path.cwd() / SRC_FOLDER).iterdir()]
mosaic, out_trans = merge(src_images)

out_meta = src_images[0].meta.copy()
out_meta.update({"driver": "GTiff",
                 "height": mosaic.shape[1],
                 "width": mosaic.shape[2],
                 "transform": out_trans,
                 "crs": "+proj=utm +zone=35 +ellps=GRS80 +units=m +no_defs "
                 }
                )

with rasterio.open(Path(OUT_FOLDER) / 'mosaic.tif', "w", **out_meta) as dest:
    dest.write(mosaic)
