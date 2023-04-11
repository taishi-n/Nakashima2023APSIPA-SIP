#!/usr/bin/env perl
# # for English
# $latex          = 'pdflatex -synctex=1 -halt-on-error';
# $latex_silent   = 'pdflatex -synctex=1 -halt-on-error -interaction=batchmode';

# for Japanese
$latex          = 'platex -synctex=1 -halt-on-error';
$latex_silent   = 'platex -synctex=1 -halt-on-error -interaction=batchmode';
$dvipdf         = 'dvipdfmx -V 7 %O -o %D %S';

# common
$bibtex         = 'bibtex';
$biber          = 'biber --bblencoding=utf8 -u -U --output_safechars';
$makeindex      = 'mendex %O -o %D %S';
$max_repeat     = 5;
$pdf_mode       = 3;
$pvc_view_file_via_temporary = 0;
$out_dir = 'build';
