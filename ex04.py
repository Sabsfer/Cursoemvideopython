medida=float(input('digite uma distância em metros:'))
km=medida/1000
hm=medida/100
dam=medida/10
dm=medida*10
cm=medida*100
mm=medida*1000
print('medida de {}m é igual a:\nkm:{}\nhm:{}\ndam:{:.0f}\ndm:{:.0f} \ncm:{:.0f}\nmm:{:.0f}'.format(medida,km,hm,dam,dm,cm,mm))
