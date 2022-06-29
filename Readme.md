# Readme

В этом репозитории вы можете найти лабораторные работы по курсу общей физики МФТИ за 3й и 4 семестры. Лабораторные работы выполнены с помощью Latex и открыты к использованию.

## Структура папок

В каждой папке содержится лабораторная работа с соответствующим номером. Для удобства файлы разделены по папкам:

- _include_ содержит файлы .tex, вкдючаемые в основной документ: preambule (файл с настройками документа), title (титульник)
- _images_ содержит картинки, вставляемые в итоговый документ (иллюстрации, графики и др)
- _data_ содержит файлы с эксперементальными данными (как правило это таблицы .ods)
- _python_ содержит python скрипты для построения графиков. Для облегчения написания кода в каждой такой папке содержится файл __PythonGraphMod.py__ который соержит авторские модули и функции для построения. Код сожержит комментарии, при желании читатель может ознакомиться с ним.
- _tables_ содержит отдельные .tex файлы, содержащие только таблицы. Данные файлы в последствии подключаются в основной документ. Сделано это для того, чтобы не загромодать итоговый исходный код.

Основной документ имеет имя main.tex и содержит основной исходный код лабораторной работы.

## Инструкция по сборке

Предоставленные материалы можно использовать как для чисто визуального ознакомления (для этого в каждой папке содержится итоговый pdf документ), так и для самостоятельной сборки и правки.

ATTENTION: при использовании шаблона лабораторной работы не забудьте внести необходимые правки в титульнике документа. Для этого перейдите в папку _include_ соответствующей лабораторной работы, откройте файл __title.tex__ и внесите необходимые изменения (все редактируемый поля отмечены соответствующими комментариями).

___

При разработке сборка проекта производилась на OS Linux Ubuntu.
Для сборки проекта необходимо установить следующие пакеты:
```
sudo apt-get install texlive-latex-base
sudo apt-get install texlive-fonts-recommended
sudo apt-get install texlive-fonts-extra
sudo apt-get install texlive-latex-extra
```

Скопируйте проект в рабочую директорию вашего ПК, используя команду
```
git clone https://github.com/pavel-collab/MIPT_Labs.git
```

Чтобы запустить автоматическую сборку в рабочей директории неободимо выполнить команду
```
pdflatex main.tex
``` 
при этом в текущей директории будет создано несколько вспомогательных файлов с расширениями
.aux, .bbl, .blg, .log, .out, .toc и, возможно, несколько других, а так же основной файл Differential_equations.pdf.

Для того, чтобы отчистить рабочую директорию от вспомогательных файлов в каждой папке предусмотрен скрипт _clean.sh_. Для исполнения этого файла, вам необходимо сначала присвоить ему соответсвующие права командой
```
chmod +x clean.sh
```
после чего запустить его
```
./clean.sh
```
при этом будут удалены все вспомогательные файлы, а основной pdf документ останется в директории.
Для повторной сборки проекта снова выполните команду ```pdflatex main.tex```.

### Сборка в онлайн редакторе Overleaf

Сборку данного проекта возможно провести в онлайн Latex редакторе Overleaf. Для этого необходимо иметь аккаунт на сайте [https://ru.overleaf.com/login](https://ru.overleaf.com/login). Сознайде новый проект и удалите все автоматически созданные файлы. Загрузите с вашего компьютера все файлы и папки, кроме _clean.sh_, откройте в Overleaf файл main.tex и нажмите на кнопку __Recompile__.

ATTENTION: для того, чтобы корректно скомпилировать проект в Overleaf необходимо перейдите в папку _include_ и перенесите строчку __\documentclass[a4paper, 12pt]{article}__ в начало файла _main.tex_.

## Несколко полезных вещей, если вы пишете на Linux

To copy basic files from Template/ to directory with labwork on Linux use:
```
mkdir <lab_dir>
cd Template
cp -r * ../<lab_dir>/
```

To use latex indent utilite:
```
latexindent main.tex -o=new_main.tex
```
where new_main.tex is a new main source
