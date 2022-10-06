
lomin=96
lomax=108
lamin=21
lamax=35
freq_array=(0.2218)

for freq in ${freq_array[*]}
do
    lo=$lomin
    while [ `echo "$lo<=$lomax"|bc` -eq 1 ]
    do
        la=$lamin
        while [ `echo "$la<=$lamax"|bc` -eq 1 ]
        do
            #输出：modcus$phvel.d
            sh 1_get_1D_model.sh $lo $la phvel
            phvel=`sh 2_phvel_compute.sh $freq modcusphvel.d`

            echo "$lo $la $phvel">>"f_"${freq}".phvel.txt"
        la=`echo "scale=1; ${la}+0.5 "|bc`
        done
    lo=`echo "scale=1; ${lo}+0.5 "|bc`
    done
done
