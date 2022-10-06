##eg: sh phvel_compute.sh 0.05
##计算输入频率和模型的相速度，输出相速度到屏幕

if [ $# -ne 2 ]
then
	echo "parameter of freq needed. eg: 0.05 modcus.d"
	exit 8
fi

f=$1
model=$2
{
sprep96 -M $model -HS 20 -HR 0 -R -FREQ $f -NMOD 1
sdisp96 -R
sdpsrf96 -R -TXT
}>/dev/null

phvel=`cat SDISPR.TXT |awk -F ' ' '{if(NR==7)print$3}'`
echo "$phvel"