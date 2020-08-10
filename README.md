[![Current PyPI packages](https://badge.fury.io/py/spacy-chapas.svg)](https://pypi.org/project/spacy-chapas/)

# spaCy-ChaPAS

ChaPAS-CaboCha-MeCab wrapper for spaCy

## Basic Usage

```py
>>> import spacy_chapas
>>> nlp=spacy_chapas.load()
>>> doc=nlp("太郎は花子が読んでいる本を次郎に渡した")
>>> for t in doc:
...   print(t.i,t.orth_,t.lemma_,t.pos_,t.tag_,t.head.i,t.dep_,t.norm_,t.ent_iob_,t.ent_type_)
...
0 太郎 太郎 PROPN 名詞-固有名詞-人名-名 12 nsubj タロウ B PERSON
1 は は ADP 助詞-係助詞 0 case ハ O
2 花子 花子 PROPN 名詞-固有名詞-人名-名 4 nsubj ハナコ B PERSON
3 が が ADP 助詞-格助詞-一般 2 case ガ O
4 読ん 読む VERB 動詞-自立 7 acl ヨン O
5 で で CCONJ 助詞-接続助詞 4 mark デ O
6 いる いる AUX 動詞-非自立 4 aux イル O
7 本 本 NOUN 名詞-一般 12 obj ホン O
8 を を ADP 助詞-格助詞-一般 7 case ヲ O
9 次 次 NOUN 名詞-一般 10 compound ツギ O
10 郎 郎 NOUN 名詞-一般 12 obl ロウ O
11 に に ADP 助詞-格助詞-一般 10 case ニ O
12 渡し 渡す VERB 動詞-自立 12 ROOT ワタシ O
13 た た AUX 助動詞 12 aux タ O
>>> import deplacy
>>> deplacy.render(doc,Japanese=True)
太郎 PROPN ═╗<══════════╗ nsubj(主語)
は   ADP   <╝           ║ case(格表示)
花子 PROPN ═╗<╗         ║ nsubj(主語)
が   ADP   <╝ ║         ║ case(格表示)
読ん VERB  ═══╝═╗═╗<╗   ║ acl(連体修飾節)
で   CCONJ <════╝ ║ ║   ║ mark(標識)
いる AUX   <══════╝ ║   ║ aux(動詞補助成分)
本   NOUN  ═╗═══════╝<╗ ║ obj(目的語)
を   ADP   <╝         ║ ║ case(格表示)
次   NOUN  <╗         ║ ║ compound(複合)
郎   NOUN  ═╝═╗<╗     ║ ║ obl(斜格補語)
に   ADP   <══╝ ║     ║ ║ case(格表示)
渡し VERB  ═╗═══╝═════╝═╝ ROOT(親)
た   AUX   <╝             aux(動詞補助成分)
```

`spacy_chapas.load(UniDic)` loads spaCy Language pipeline for ChaPAS-CaboCha-MeCab. Available `UniDic` options are:

* `UniDic="gendai"`: Use [現代書き言葉UniDic](https://unidic.ninjal.ac.jp/download#unidic_bccwj).
* `UniDic="spoken"`: Use [現代話し言葉UniDic](https://unidic.ninjal.ac.jp/download#unidic_csj).
* `UniDic="qkana"`: Use [旧仮名口語UniDic](https://unidic.ninjal.ac.jp/download_all#unidic_qkana).
* `UniDic="kindai"`: Use [近代文語UniDic](https://unidic.ninjal.ac.jp/download_all#unidic_kindai).
* `UniDic="kinsei"`: Use [近世口語（洒落本）UniDic](https://unidic.ninjal.ac.jp/download_all#unidic_kinsei).
* `UniDic="kyogen"`: Use [中世口語（狂言）UniDic](https://unidic.ninjal.ac.jp/download_all#unidic_kyogen).
* `UniDic="wakan"`: Use [中世文語（説話・随筆）UniDic](https://unidic.ninjal.ac.jp/download_all#unidic_wakan).
* `UniDic="wabun"`: Use [中古和文UniDic](https://unidic.ninjal.ac.jp/download_all#unidic_wabun).
* `UniDic="manyo"`: Use [上代（万葉集）UniDic](https://unidic.ninjal.ac.jp/download_all#unidic_manyo).
* `UniDic=None`: Use IPADic (default).

You can simply use `chapas2ud` on the command line to get [Universal Dependencies](https://universaldependencies.org/format.html):

```sh
echo 太郎は花子が読んでいる本を次郎に渡した | chapas2ud -I RAW
```

Try [notebook](https://colab.research.google.com/github/KoichiYasuoka/spaCy-ChaPAS/blob/master/spacy_chapas.ipynb) for Google Colaboratory.

## Installation for Linux (Debian)

First, install [MeCab](https://taku910.github.io/mecab/) and necessary packages:

```sh
sudo apt update
sudo apt install mecab libmecab-dev mecab-ipadic-utf8 python3-pip python3-dev g++ make curl openjdk-8-jre-headless
cd /tmp
curl -L 'https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7QVR6VXJ5dWExSTQ' | tar xzf -
cd CRF++-0.58
./configure --prefix=/usr --libdir=`mecab-config --libs-only-L`
make && sudo make install
```

Second, install [CaboCha](https://taku910.github.io/cabocha/):

```sh
cd /tmp
curl -sc cabocha.cookie 'https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7SDd1Q1dUQkZQaUU' > /dev/null
curl -Lb cabocha.cookie 'https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7SDd1Q1dUQkZQaUU&confirm='`tr -d '\015' < cabocha.cookie | awk '/_warning_/{print $NF}'` | tar xjf -
cd cabocha-0.69
./configure --prefix=/usr --libdir=`mecab-config --libs-only-L` --with-charset=UTF8
make && sudo make install
```

Third, install [ChaPAS](https://sites.google.com/site/yotarow/chapas):

```sh
cd /tmp
curl -sc chapas.cookie 'https://drive.google.com/uc?export=download&id=0BwG_CvJHq43fNDlqSkVSREkzaEk' > /dev/null
curl -Lb chapas.cookie 'https://drive.google.com/uc?export=download&id=0BwG_CvJHq43fNDlqSkVSREkzaEk&confirm='`tr -d '\015' < chapas.cookie | awk '/_warning_/{print $NF}'` | tar xzf -
sudo mkdir -p /usr/local/bin
sudo mv chapas-0.742 /usr/local/chapas
( echo '#! /bin/sh' ; echo exec `ls -1 /usr/lib/jvm/j*-1.8.*/bin/java | tail -1` -Xmx1g -jar /usr/local/chapas/chapas.jar '"$@"' ) > chapas
sudo install chapas /usr/local/bin
```

And last, install spaCy-ChaPAS:

```sh
pip3 install spacy_chapas --user
```

## Installation for Linux (Ubuntu)

Same as Debian.

## Installation for Linux (Kali)

Same as Debian.

## Installation for Linux (CentOS)

First, install [MeCab](https://taku910.github.io/mecab/) and necessary packages:

```sh
sudo yum update
sudo yum install python3-pip python3-devel gcc-c++ make curl bzip2 java-1.8.0-openjdk-headless epel-release
sudo rpm -ivh https://packages.groonga.org/centos/latest/groonga-release-latest.noarch.rpm
sudo yum install mecab mecab-devel mecab-ipadic
cd /tmp
curl -L 'https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7QVR6VXJ5dWExSTQ' | tar xzf -
cd CRF++-0.58
./configure --prefix=/usr --libdir=`mecab-config --libs-only-L`
make && sudo make install
```

Second, third, and last are same as Debian.

## Installation for Cygwin64

Make sure to get `python37-devel` `python37-pip` `python37-cython` `python37-numpy` `git` `gcc-g++`, and then:

```sh
pip3.7 install git+https://github.com/KoichiYasuoka/chapas-cygwin64
pip3.7 install spacy_chapas --no-build-isolation
```

