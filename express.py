

lista_premio = ["F-9416-E50B-DEED",
"C-F833-CA3B-DF0A ",
"D-AC63-3D2F-DEF7 ",
"1-3C1B-D6D7-DEEF ",
"5-E8A4-B1B3-DF09 ",
"A-E823-86AD-DEDC",
"4-BC11-D103-DEA9 ",
"1-D04D-F3CB-DF0C ",
"6-1413-1B7B-DEBF" ,
"A-001C-ABD3-DE9D" ,
"8-B030-D7BB-DE9C" ,
"D-AC18-7FB1-DEBD" ,
"B-E01F-248D-DE9E" ,
"3-B016-A8F5-DEBC" ,
"D-D43F-8857-DED8" ,
"1-481B-66FD-DEA9" ,
"F-D43C-A12F-DF0A" ,
"3-AC2C-FD23-DED1" ,
"4-F819-CAD1-DF0A" ,
"F-581E-1C13-DEEA" ,
"C-CC54-7459-DEAB" ,
"0-1423-147D-DF07" ,
"5-301E-9299-DEE5" ,
"E-B014-DC4D-DEEE" ,
"F-A021-0F05-DEC7" ,
"D-8018-06A3-DED8" ,
"4-F432-135F-DEB8" ,
"6-B41C-E8CB-DEFE" ,
"1-4817-A8BD-DF05" ,
"F-F026-0BE1-DEB5" ,
"1-3C10-D781-DEDA",
"F-E416-BAFD-DEB0" ,
"4-D4AA-5583-DEB2",
"E-2C16-249D-DED0",
"4-142D-1CEF-DEB0" ,  
"E-F49E-86AD-DEF7",  
"C-5C25-3C0D-DEBD",
"8-2827-A7BD-DEA3",
"8-C48C-C147-DEB9", 
"5-703D-A4C9-DEA1",  
"5-E080-1435-DEC4", 
"B-8036-63B5-DECA",   
"A-F81C-BFED-DEC6",  
"4-DC15-50B7-DEB4", 
"6-3021-7133-DF0A", 
"2-3C5F-9F21-DEE7",  
"F-A83C-5C03-DEEE",  
"3-202E-5023-DEDB",  
"D-D822-0F49-DE9C",  
"8-7C22-87F9-DE9F",  
"E-1C3E-A3B7-DEE0", 
"3-3831-7B5F-DF0A",  
"0-8042-F4BD-DED5",   
"D-4831-46DD-DEC9",   
"6-DC5D-0171-DF0B",   
"9-4C2E-FD5D-DF00",  
"F-B03E-1F1B-DEC0",   
"E-3054-9C01-DEA8",       
"E-1024-E3FF-DEBB",        
"2-442E-08E1-DEF6",        
"B-180D-FE7D-DEF2",        
"B-A420-1249-DEFA",       
"E-E816-ED83-DEC5",       
"4-8810-F33D-DEE7",       
"9-C03A-E68F-DEB2",       
"6-3814-8D55-DF03",     
"6-702A-C9D3-DED1",     
"C-EC1E-5693-DEA6",     
"E-1C1B-D1C5-DEA3",       
"A-6423-24EB-DEB7",       
"B-2853-C45F-DF0B",      
"8-C459-947F-DF02",      
"6-540C-E4DD-DEDA",       
"A-E887-F977-DEFE",    
"E-1820-17DD-DEC8",      
"1-0435-785B-DEFE",      
"5-5C28-FB93-DEBB",       
"D-A84C-DD61-DEBD",      
"5-4843-9357-DEA8",      
"2-6023-C6EB-DED8",       
"C-6030-B901-DEDA",       
"E-2C40-3265-DEE0",       
"3-0C2E-65D9-DEFA",     
"9-A432-14BD-DEDF",      
"B-5019-535B-DECB",       
"1-941A-BE6D-DED2",     
"4-C425-F447-DF0B",       
"2-9820-3891-DEC2",      
"F-001C-21D3-DEC3",       
"1-6C39-B16F-DF09",      
"8-6825-E90B-DED3",       
"0-3C64-8EAF-DEC7",       
"6-A42D-C763-DEBE",       
"4-CC3F-04CD-DF09",       
"2-941D-4F7D-DEAB",       
"A-583D-D6B7-DEFE",       
"A-0429-9B9B-DEF9",       
"3-1411-CA8D-DF00",       
"7-E414-893B-DEAB",       
"8-1C2E-AAD5-DED8"]

 #"8-1C2E-AAD5-DED8"

boleto_ganador = input("coloca el numero de ticket:" )

for ticket in lista_premio:
    if ticket == boleto_ganador:
        print("usted acaba de ganarse un carro ")
        break

else:
    print("usted se guallo bien feo")
       

