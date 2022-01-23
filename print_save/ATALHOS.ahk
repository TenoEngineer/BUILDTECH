;ATALHOS

;PREENCHIMENTO AUTOMATICO
::ccc::TP 138 daN CORDOALHA - CLIENTE(P)
::nnn::TP 184 daN 500JCA - NET
::xxx::TP 54 daN 12 FAS - 
::caca::CA 40-50 - OI
::ct48::TP 77 daN 48 FAS - CLIENTE(P)
::ct36::TP 77 daN 36 FAS - CLIENTE(P)
::ct24::TP 64 daN 24 FAS - CLIENTE(P)
::ct12::TP 54 daN 12 FAS - CLIENTE(P)
::ct04::TP 54 daN 04 FAS - CLIENTE(P)
::splitt::[BASENAME]_[FILENUMBER]
;::mx::MT3#70mm2XPLE  ARRUMAR
;::bx::BT3#50(50)XPLE

;F1 PARA DEL
F1::
Send, {DEL}
return

;PRINT CALCULO
#q::
Run "C:\Users\heito\BUILDTECH\print_save\main.py"
return
