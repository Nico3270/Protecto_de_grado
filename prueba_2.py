import capacidad_NS as cap

def Capacidad_Ns(a_carril, a_berma, p_promedio, l_sector, d_sentido, p_no_rebase, p_autos, p_buses, p_camiones, vol_cap):
    p_pesados = p_buses+p_camiones
    c_ideal = 3200
    #Capacidad
    Fpe = cap.inter_compuesta_1(p_promedio, cap.tabla_1x, cap.tabla_1, l_sector)
    Fd = cap.inter_compuesta_2(d_sentido,cap.tabla_2x,cap.tabla_2,p_no_rebase)
    Fcb = cap.inter_compuesta3(cap.tabla_3x,cap.tabla_3,a_berma,a_carril)
    Ec = cap.inter_compuesta4(cap.tabla_4x, cap.tabla_4, p_promedio, p_pesados, l_sector)
    Fp = (1/(1+(p_pesados/100)*(Ec-1)))
    Fp = round(Fp,4)
    cap_60 = round(c_ideal*Fpe*Fd*Fcb*Fp,0)
    FHP = cap.inter_tabla5(cap.tabla_5,cap.tabla_5x,cap.tabla_51,cap.tabla_51x,cap_60)
    cap_5 =round(cap_60*FHP,0)
    #Nivel de servico
    v1 = cap.inter_compuesta6(cap.tabla_6x, cap.tabla_6, p_promedio, l_sector)
    Fu = cap.interpolacion(cap.tabla_7x,cap.tabla_7,vol_cap/cap_60)
    Fcb1 = cap.inter_compuesta8(cap.tabla_8x,cap.tabla_8,a_carril,a_berma)
    v2 = v1* Fu * Fcb1
    print(v2)
    Ec_vel = 0
    if p_promedio < 3:
        Ec_vel = cap.inter_compuesta_plan_ond(v2,cap.tabla_9x,cap.plano,p_camiones,l_sector)
    elif  p_promedio < 6:
        Ec_vel = cap.inter_compuesta_plan_ond(v2,cap.tabla_9x,cap.ondulado,p_camiones,l_sector)
    elif  p_promedio <9:
        Ec_vel = cap.inter_compuesta_mon_esc(v2,cap.tabla_9x,cap.montanoso,p_camiones,l_sector)
    else:
        Ec_vel = cap.inter_compuesta_mon_esc(v2,cap.tabla_9x,cap.escarpado,p_camiones,l_sector)

    fp_vel = round(1/(1+((p_camiones/100)*(Ec_vel-1))),3)
    Ft = round(cap.interpolacion(cap.tabla_10x, cap.tabla_10, p_promedio),3)
    vM = v2*fp_vel*Ft
    Vi = int((vM * 100)/90)

    lista =[]
    if p_promedio < 3:
        lista = cap.plano_1
    elif  p_promedio < 6:
        lista = cap.ondulado_1
    elif  p_promedio <9:
        lista = cap.montanoso_1
    else:
        lista = cap.escarpado_1
    final = cap.index(lista, Vi)
    return  Fpe,Fd,Fcb,Ec,Fp,cap_60,cap_5,FHP,v1,Fu,Fcb1,v2,Ec_vel,fp_vel,Ft,vM,Vi,final
rel = Capacidad_Ns(3.3,1,7,1,52,80,50,10,40,650)
print(f"La capacidad de la vía es {int(rel[5])} vehiculos y el nivel de servicio {rel[17]}")