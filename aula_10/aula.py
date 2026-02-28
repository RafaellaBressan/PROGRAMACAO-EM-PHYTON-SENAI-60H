from colorama import Fore, Back, Style,init, deinit
init()
# verificar a valor_hora
def verificar_valor_hora(carga,salario):
    return salario / carga

# verificar quantidade de horas extras
def quantidade_extra(valor_extra, valor_hora ):
    return valor_extra * valor_hora

# calculo do valor da hora extra total
def hora_extra_receber(quantidade, hora_extra):
    return quantidade *  hora_extra

# somar com o salario
def salario_bruto(salario, hora_extra_receber):
    return salario +  hora_extra_receber

# verificar os descontos  vt, vr
def descontos(salario_bruto, vt, vr):
    return salario_bruto - (vt+ vr)

# liquido e o bruto
def salario_liquido(salario_receber):
    return salario_receber


def sistema_rh():
    while True:
        print(Fore.WHITE+  '***' * 10)
        print('Calcule o salario: ')
        salario = float(input('Salário R$: '))
        carga   = 220
        # print('VERIFIQUE O SALÁRIO A RECEBER: ')
        valor_hora = verificar_valor_hora(carga,salario)
        print(Fore.GREEN + 'Valor hora R$ ', round(valor_hora,2))
        print('***' * 10)
        extra_50 = quantidade_extra(1.5, valor_hora )
        extra_100 = quantidade_extra(2.0, valor_hora )
        print(Fore.RED + 'Extra 50% - ', round(extra_50,2))
        print(Fore.BLUE +'Extra 100% - ', round(extra_100,2))
        print('***' * 10)
        quantidade_50 = float(input('quantidade de extra realizada 50%:  '))
        quantidade_100 = float(input('quantidade de extra realizada 70%:  '))

        hora_receber_50 = hora_extra_receber(quantidade_50, extra_50)
        hora_receber_100 = hora_extra_receber(quantidade_100, extra_100)
        print(f'''
              
           { Fore.RED }hora extra 50% -  R$ {round(hora_receber_50,2)}
           { Fore.RED } hora extra 100% - R$ {round(hora_receber_100,2)} 

         ''')
        
        print('***' * 10)
        hora_extra_total = hora_receber_50  +  hora_receber_100 
        salario_b = salario_bruto(salario, hora_extra_total)
        print('SALARIO BRUTO: R$ ', round(salario_b,2))

        print('DESCONTOS: ')

        salario_liquidoo =  descontos(salario_b, 250.0, 250.0)
        print(f'SALARIO A RECEBER - R$ {salario_liquidoo:.2f}')
        

sistema_rh()

