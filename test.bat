@echo off
echo .
echo .
echo .............................................
python shakers.py email anonymous mypw --param id pw --uri https://account.samsung.com/login? --postp "=" --sep "&" --cmds "curl -X POST" "curl -X GET"

echo .
echo .
echo .............................................
python shakers.py my query --uri "https://sample.com?" --param "data"

echo .
echo .
echo .............................................
python shakers.py a b


echo .
echo .
echo .............................................
echo lists = cmd * uri * ( valuex ** param )


@echo on
