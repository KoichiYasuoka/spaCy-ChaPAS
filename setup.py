import setuptools

with open("README.md","r",encoding="utf-8") as r:
  long_description=r.read()
URL="https://github.com/KoichiYasuoka/spaCy-ChaPAS"

setuptools.setup(
  name="spacy_chapas",
  version="0.6.5",
  description="ChaPAS-CaboCha-MeCab wrapper for spaCy",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url=URL,
  author="Koichi Yasuoka",
  author_email="yasuoka@kanji.zinbun.kyoto-u.ac.jp",
  license="MIT",
  keywords="spacy nlp",
  packages=setuptools.find_packages(),
  install_requires=["spacy>=2.2.2","deplacy>=1.8.7"],
  python_requires=">=3.6",
  package_data={"spacy_chapas":["./chapas2ud","./unidic2ipadic"]},
  data_files=[("bin",["spacy_chapas/chapas2ud"])],
  classifiers=[
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
    "Topic :: Text Processing :: Linguistic",
    "Natural Language :: Japanese"
  ],
  project_urls={
    "ChaPAS":"https://sites.google.com/site/yotarow/chapas",
    "CaboCha":"https://taku910.github.io/cabocha/",
    "MeCab":"https://taku910.github.io/mecab/",
    "Source":URL,
    "Tracker":URL+"/issues"
  }
)
