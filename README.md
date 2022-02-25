# Implement  and  demonstrate  the  FIND-S  algorithm  for  finding  the  most  specific hypothesis  based  on  a  given  set  of  training  data  samples.  Read  the  training  data  from  a  .CSV file. 

FIND-S  Algorithm 

1.  Initialize  h  to  the  most  specific  hypothesis  in  H 
2.  For  each  positive  training  instance  x 
3.     For  each  attribute  constraint  ai  in  h 
4.        If  the  constraint  ai  is  satisfied  by  x 
5.              Then  do  nothing 
6.        Else  replace  ai  in  h  by  the  next  more  general  constraint  that  is  satisfied  by  x 
7.  Output  hypothesis  h
