from simple_image_download import simple_image_download as simp
response = simp.simple_image_download
keywords = ["mark zukar burg"] //search images

for kw in keywords:
  response().download(kw,200)
