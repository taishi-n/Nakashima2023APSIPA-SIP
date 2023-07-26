#!/usr/bin/env perl
@default_files  = ('./Nakashima2023APSIPA-SIP.tex');
# # for English
# $latex          = 'pdflatex -synctex=1 -halt-on-error';
# $latex_silent   = 'pdflatex -synctex=1 -halt-on-error -interaction=batchmode';
# $pdf_mode       = 1;

# for Japanese
$latex          = 'platex -synctex=1 -halt-on-error';
$latex_silent   = 'platex -synctex=1 -halt-on-error -interaction=batchmode';
$dvipdf         = 'dvipdfmx -V 7 %O -o %D %S';
$pdf_mode       = 3;

# common
$bibtex         = 'pbibtex';
$biber          = 'biber --bblencoding=utf8 -u -U --output_safechars';
$max_repeat     = 5;
$pvc_view_file_via_temporary = 0;
$out_dir = 'build';
