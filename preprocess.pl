#!/usr/bin/perl

use utf8;
use Encode;

open(INPUT, "< climate_data_miyako.csv");

while($line = <INPUT>) {

  $line =~ s/[)]//g;
  print encode('utf-8',$str);
  print $line;
}
