"""
CONSTANTE = "Variaveis" que não vão mudar
Muitas condições no mesmo is(ruim)
  <- Contagem de complexidade(ruim)
"""
velocidade = 61 #velocidade atual do carro 
local_carro = 101 # local em que o carro esta na estrada

RADAR_1 = 60 #velocidade maxima do radar 1
LOCAL_1 = 100 #local onde o radar 1 esta 
RADAR_RANGE = 1 # A distancia onde o radar pega

vel_car_pas_radar_1 = velocidade > RADAR_1
carro_passou_1 = local_carro >= (LOCAL_1 + RADAR_RANGE) and \
    local_carro <= (LOCAL_1 - RADAR_RANGE)
multado_carro = carro_passou_1 and vel_car_pas_radar_1


 
if vel_car_pas_radar_1 :

    print('velocidade carro passou do radar 1')

if carro_passou_1:
   print('carro passou no radar 1 ')

if  multado_carro :

  print('Carro multado em radar 1')