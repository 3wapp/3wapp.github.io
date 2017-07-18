# patool 解压

[https://github.com/wummel/patool](https://github.com/wummel/patool)

patool 是一个压缩和解压缩工具，可对压缩包进行创建、解压、提取、测试、列表、搜索、比较和重新打包

## install

`pip install patool`

## 支持的格式

patool 支持的文件格式如下，部分文件格式需要外部程序处理压缩格式, 例如 unrar 程序处理RAR(.rar, .cbr)压缩格式

```
7z (.7z, .cb7), ACE (.ace, .cba), ADF (.adf), ALZIP (.alz), APE (.ape), AR (.a), ARC (.arc), ARJ (.arj), BZIP2 (.bz2), CAB (.cab), COMPRESS (.Z), CPIO (.cpio), DEB (.deb), DMS (.dms), FLAC (.flac), GZIP (.gz), ISO (.iso), LRZIP (.lrz), LZH (.lha, .lzh), LZIP (.lz), LZMA (.lzma), LZOP (.lzo), RPM (.rpm), RAR (.rar, .cbr), RZIP (.rz), SHN (.shn), TAR (.tar, .cbt), XZ (.xz), ZIP (.zip, .jar, .cbz), ZOO (.zoo)
```

以下格式原生支持，不需要外部程序依赖

```
TAR, ZIP, BZIP2, GZIP
```

### 外部程序依赖

| archive | file extension | ubuntu |
| --- | ---- | --- |
| RAR | .rar, .cbr | unrar |
| 7z | .7z, .cb7 | p7zip-full |

## 格式识别

patool 调用 `file` 程序识别文件压缩格式

```
file --brief --mime-type <filename>
```

## api

```Python
import patoolib

patoolib.extract_archive("archive.zip", outdir="/tmp")
patoolib.test_archive("dist.tar.gz", verbosity=1)
patoolib.list_archive("package.deb")
patoolib.create_archive("/path/to/myfiles.zip", ("file1.txt", "dir/"))
patoolib.diff_archives("release1.0.tar.gz", "release2.0.zip")
patoolib.search_archive("def urlopen", "python3.3.tar.gz")
patoolib.repack_archive("linux-2.6.33.tar.gz", "linux-2.6.33.tar.bz2")
```
