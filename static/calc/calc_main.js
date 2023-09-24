//  *******************************************
//***        REMONT199.COM calculator         ***
// ********************************************


moneyCalc={
  usdOld:36,
  usdToday:0,
  
  r_length:0,
  r_width:0,
  r_height:0,
  perimetr:0,
  sq_wall:0,
  square: 0, //Площадь

  gruntPrice:45, // грунтовка;
  paint:225, // покраска
  
  removeWhitewashPrice:250, //Удаление побелки, краски
  ceilingPlasterPrice:1000 ,//Штукатурка потолка
  ceilingGKLPrice:900, //Подвесной потолок из ГКЛ
  ceilingPuttyForPaintPrice:610, //шпаклевка потолка под покраску
  galtelPrice:170, //потолочный плинтус
  galtelPaintPrice:165, //потолочный плинтус покраска
  
  
  removeWallpaperPrice:200, //Удаление обоев
  wallPlasterPrice:500, //штукатурка стен
  wallPuttyForWallpaper:425, //шпаклевка под обои
  wallPaper:350, //поклейка обоев
  wallPuttyForPaint:190 ,//шпаклевка под покраску финишный слой
  decorativePaint:750, //декоративная краска

  removeOldFloor:300,  //удаление старого пола
  floorLeveling:500, //выравнивание пола
  superFloor:610, //KNAUF супер пол
  paroizol:80,//пароизоляционная пленка
  keramzit: 150, //Засыпка керамзита под стяжку
  floorPlinth:200, //плинтус напольный
  laminat:600, //ламинат
  floorTiles:1200, //напольная плитка
  floorFlooring:800, //паркетная доска
  linoleum:250, //линолеум  
  
  ceilingSum: 0, //сумма за потолок
  wallSum: 0,    //сумма за стены
  floorSum: 0,   //сумма за пол
  allSum: 0,     //итог за работы

  dWidth : 0,
  dSum : 0,  
  verbose: 1,
  
}





 moneyCalc.roomScan = function() {
 //    принимает тип комнаты
  var roomType = document.getElementById("roomType"); //link on element 'select'
  var result = 0;
  result += parseInt(roomType.options[roomType.selectedIndex].value);
 
  //     в зависимости от выбора разблокирует div
  if (result == 1)
  {
    var es = document.getElementById("simple");
    es.style.cssText="display:block;";   
    var el = document.getElementById("complicated");
    el.style.cssText="display:none;";     
  }
  else if (result == 2)
  {
    var el = document.getElementById("complicated");
    el.style.cssText="display:block;";   
    var es = document.getElementById("simple");
    es.style.cssText="display:none;";        
  }
  perimetr = 0;
  //получение введенных значений
  //длина
  var l = document.getElementById("length");
  var r_length = parseFloat(l.value);
  
  //ширина
  var wi = document.getElementById("width");
  var r_width = parseFloat(wi.value); 
  
  //высота
  var h = document.getElementById("height");
  var r_height = parseFloat(h.value);
  

  if (isNaN(perimetr) || isNaN(r_height) || isNaN(r_width) || isNaN(r_length))
  {
    perimetr = 0; 
    r_length = 0; 
    r_width = 0;
    r_height = 0;
  }  
  
  var w = document.getElementById("sq_walls");// получаем ссылку на элемент span, в него будем писать площадь
  var c = document.getElementById("sq_ceiling");// получаем ссылку на элемент span, в него будем писать площадь
  
  var sq_windows = 0; //окно 
   var wHeight = parseFloat(document.getElementById("wHeight").value);
   var wWidth = parseFloat(document.getElementById("wWidth").value);
   var wSum = parseFloat(document.getElementById("wSum").value);
   sq_windows = wHeight * wWidth * wSum;
  
  var sq_doors = 0; //дверi
   var dHeight = parseFloat(document.getElementById("dHeight").value);
   var dWidth = parseFloat(document.getElementById("dWidth").value);
   var dSum = parseFloat(document.getElementById("dSum").value);
   sq_doors = dHeight * dWidth * dSum;  
   this.dWidth = dWidth;
   this.dSum = dSum;
  
  if (result === 2) // если выбран сложный тип помещения
   {
     //периметр
     var p = document.getElementById("perimetr");
     this.perimetr = parseFloat(p.value).toFixed(2);
     this.square = parseFloat(c.value).toFixed(2);
     r_length = 0;
     r_width = 0;
  } else if (result === 1) //если выбран простой тип помещения
   {
     this.perimetr = parseFloat((r_length + r_width) * 2).toFixed(2);
     this.square = (r_length * r_width).toFixed(2);
     c.value = parseFloat(this.square).toFixed(2);
  } else {
     this.square = 0;
  }




  this.sq_wall = ((this.perimetr * r_height) - sq_doors - sq_windows).toFixed(2);
  if (this.sq_wall < 0)
  {
    this.sq_wall = 0 ;
  }
  
  w.innerHTML = this.sq_wall;
//  c.value = this.sq_ceiling.toFixed(2);
  //  f.innerHTML = sq_floor.toFixed(2);
  
//this.sq_ceiling = this.sq_ceiling;
  
}
moneyCalc.ceilingManual = function() {
  this.square = parseFloat(document.getElementById("sq_ceiling").value);
//  return(c);
}
moneyCalc.isDiagonal = function() {
  
  if (parseInt(floorFinish.options[floorFinish.selectedIndex].value) < 4) {
   document.getElementById("diagonal").style.display='block'; 
  }
  
  else {
   document.getElementById("diagonal").style.display='none'; 
  }    
}



////////////////////////////////////
//////// CALCULATOR ///////////////
////////////////////////////////////

moneyCalc.calculateAll = function(verb) {

   this.verbose = verb

   
/*  	  var d = document.createElement('div');
  d.className='color';
  document.body.appendChild(d);*/

///***************Цены*****************////////////
  var toFixedNumber = 2
//   alert(moneyCalc.usdToday)
  var usdRatio = this.usdToday / this.usdOld
   //alert(usdRatio)
  var removeWhitewashPrice = Math.round(this.removeWhitewashPrice * usdRatio / 10) * 10 //Удаление побелки, краски
  var gruntPrice = Math.round(this.gruntPrice * usdRatio / 10) * 10 // грунтовка;
  var galtelPrice = Math.round(this.galtelPrice * usdRatio / 10) * 10 //потолочный плинтус
  var galtelPaintPrice = Math.round(this.galtelPaintPrice * usdRatio / 10) * 10 //покраска потолочный плинтус
  var ceilingPlasterPrice = Math.round(this.ceilingPlasterPrice * usdRatio / 10) * 10 //Штукатурка потолка
  var ceilingGKLPrice = Math.round(this.ceilingGKLPrice * usdRatio / 10) * 10 // Гипсокартон
  var ceilingPuttyForPaint = Math.round(this.ceilingPuttyForPaintPrice  * usdRatio / 10) * 10 //шпаклевка потолка под покраску
  
  var paint = Math.round(this.paint  * usdRatio / 10) * 10 // покраска

  var removeWallpaperPrice = Math.round(this.removeWallpaperPrice  * usdRatio / 10) * 10 //Удаление обоев
  var wallPlasterPrice = Math.round(this.wallPlasterPrice  * usdRatio / 10) * 10 //штукатурка стен
  var wallPuttyForWallpaper = Math.round(this.wallPuttyForWallpaper  * usdRatio / 10) * 10 //шпаклевка под обои
  var wallPaper = Math.round(this.wallPaper  * usdRatio / 10) * 10 //поклейка обоев
  var wallPuttyForPaint = Math.round(this.wallPuttyForPaint  * usdRatio / 10) * 10 //шпаклевка под покраску
  var decorativePaint = Math.round(this.decorativePaint  * usdRatio / 10) * 10 //декоративная краска

  var removeOldFloor = Math.round(this.removeOldFloor * usdRatio / 10) * 10 //удаление старого пола
  var floorLeveling = Math.round(this.floorLeveling * usdRatio / 10) * 10 //выравнивание пола
  var superFloor = Math.round(this.superFloor * usdRatio / 10) * 10 //KNAUF супер пол
  var paroizol = Math.round(this.paroizol * usdRatio / 10) * 10 //пароизоляционная пленка
  var keramzit =  Math.round(this.keramzit * usdRatio / 10) * 10 //Засыпка керамзита под стяжку
  var floorPlinth = Math.round(this.floorPlinth * usdRatio / 10) * 10 //плинтус напольный
  var laminat = Math.round(this.laminat * usdRatio / 10) * 10 //ламинат
  var floorTiles = Math.round(this.floorTiles * usdRatio / 10) * 10 //напольная плитка
  var floorFlooring = Math.round(this.floorFlooring * usdRatio / 10) * 10 //паркетная доска
  var linoleum = Math.round(this.linoleum * usdRatio / 10) * 10 //линолеум      
       

  
  
  
  
  
  ///***************Потолок*****************////////////
  clear_object(MatAmount);
  Ceiling = copy_obj(MatAmount)
//Удаление побелки, краски
  var removeWhitewash = 0; 
  if(document.getElementById('isRemoveWhitewash').checked == true) {
   removeWhitewash = removeWhitewashPrice;  	
   }
  	
 //Штукатурка 	
  var needCeilingPlaster = 0;
  if(document.getElementById('needCeilingPlaster').checked == true) {
   needCeilingPlaster = ceilingPlasterPrice;  	
   }

 //Гипсокартон 	
  var needCeilingGKL = 0;
  if(document.getElementById('needCeilingGKL').checked == true) {
   needCeilingGKL = ceilingGKLPrice;  	
   }  	

 //Шпаклевка 	
  var needCeilingPutty = 0;
  if(document.getElementById('needCeilingPutty').checked == true) {
   needCeilingPutty = ceilingPuttyForPaint + (gruntPrice * 2);  	
   } 
  	
  	
 //Потолочный плинтус (галтель)
  var needGaltel = 0;
  if(document.getElementById('needGaltel').checked == true) {
    needGaltel = this.perimetr * galtelPrice;
    needGaltel += this.perimetr * galtelPaintPrice; //Покраска галтели  	
  }   

  //Варианты отделки:
  var ceilingFinishType = document.getElementById("ceilingFinish");//получаем ссылку на элемент Select
  var ceilingTypeSelected =  parseInt(ceilingFinish.options[ceilingFinish.selectedIndex].value);
  var ceilingCoverPrice = 0 ;
  switch (ceilingTypeSelected) {
    case 0 :
      ceilingCoverPrice = 0
      break
    case 1 :
      //Покраска
      ceilingCoverPrice = gruntPrice + paint  
      break
    default :
      ceilingCoverPrice = 0
  }
  var ceilingSum = Math.round(((removeWhitewash + needCeilingPlaster + needCeilingGKL + needCeilingPutty + ceilingCoverPrice) *  this.square) + needGaltel);
  
 // alert(removeWhitewash +" + "+needCeilingPlaster+" + "+needCeilingGKL+" + "+needCeilingPutty+" + "+ceilingCoverPrice)
  document.getElementById("calcCeiling").innerHTML = ceilingSum;

 
 
  ////////////////////////////////
  //Вывод сумм по видам работ/////
  ////////////////////////////////
   
   ////// ПОТОЛОК /////////
  document.getElementById("calcCeilingExt").innerHTML = null;
//Площадь и периметр
  document.getElementById("calcCeilingExt").innerHTML = "<p>Площадь: " + this.square + " м&sup2;, периметр: " + this.perimetr + " м</p>"
  if (removeWhitewash != 0) {
//Удаление побелки, краски
     document.getElementById("calcCeilingExt").innerHTML += "<p title=\"Удаление побелки, краски, обработка бетоконтактом итп\">Подготовка поверхности (" 
     + removeWhitewash + " руб/м&sup2;): " + (this.square * removeWhitewash).toFixed(0) + " руб.</p>";
  }
//Штукатурка потолка
  if (needCeilingPlaster != 0) {
     document.getElementById("calcCeilingExt").innerHTML += "<p>Штукатурка потолка (" + needCeilingPlaster + 
     " руб/м&sup2;): " + (this.square * needCeilingPlaster).toFixed(0) + " руб.</p>";
     Ceiling.plasterThick = parseFloat(document.getElementById('ceilingPlasterThick').value).toFixed(1)
     Ceiling.beto_kont += MatConsuption.beto_kont * this.square
     Ceiling.rotband += parseInt(MatConsuption.rotband * this.square * Ceiling.plasterThick)
     
  }

//Потолок из гипсокартона 
  if (needCeilingGKL != 0) {
     document.getElementById("calcCeilingExt").innerHTML += "<p>Потолок из гипсокартона (" + needCeilingGKL + 
     " руб/м&sup2;): " + (this.square * needCeilingGKL).toFixed(0) + " руб.</p>";
     Ceiling.gkl += parseInt(this.square * 1.1);
  }
//Шпаклевка под покраску
  if (needCeilingPutty != 0) {
     document.getElementById("calcCeilingExt").innerHTML += "<p title=\"Необходимо прогрунтовать второй раз перед финишным слоем шпаклевки\">Грунтовка (2 слоя по " +
      gruntPrice + " руб/м&sup2;): " + (this.square * gruntPrice * 2).toFixed(0) + " руб.</p>";
     document.getElementById("calcCeilingExt").innerHTML += "<p>Шпаклевка под покраску (" + ceilingPuttyForPaint + 
     " руб/м&sup2;): " + (this.square * ceilingPuttyForPaint).toFixed(0) + " руб.</p>";
     Ceiling.grunt += parseInt(this.square * MatConsuption.grunt * 2)
     Ceiling.lr += parseInt(MatConsuption.lr * this.square)
     Ceiling.sheetr += parseInt(MatConsuption.sheetr * this.square)
  }

//Потолочный плинтус (галтель)
  if (needGaltel != 0) {
     document.getElementById("calcCeilingExt").innerHTML += "<p>Потолочный плинтус (монтаж, шпаклевка) (" + 
     galtelPrice + " руб/п.м.): " + (this.perimetr * galtelPrice).toFixed(0) + " руб.</p>";
     Ceiling.galtel += this.perimetr

     document.getElementById("calcCeilingExt").innerHTML += "<p>Покраска потолочного плинтуса (" + 
     galtelPaintPrice + " руб/п.м.): " + (this.perimetr * galtelPaintPrice).toFixed(0) + " руб.</p>";

  }
//ПОкраска потолка
  if (ceilingCoverPrice != 0) {
     document.getElementById("calcCeilingExt").innerHTML += "<p>Грунтовка (" + gruntPrice + " руб/м&sup2;): " + 
     (this.square * gruntPrice).toFixed(0) + " руб.</p>";
     document.getElementById("calcCeilingExt").innerHTML += "<p>Покраска (" + paint + " руб/м&sup2;): " + 
     (this.square * paint).toFixed(0) + " руб.</p>";
     Ceiling.grunt += this.square * MatConsuption.grunt
     Ceiling.paint += MatConsuption.paint * this.square
  }



  
  //////////////////////////////////////////////////////
  /////************** Стены ****************////////////
  /////////////////////////////////////////////////////
  clear_object(MatAmount);
  Wall = copy_obj(MatAmount)
  
  var getCalcWall = document.getElementById("calcWall");
  
  //Удаление старых обоев
  var isRemoveWallpaper = 0;
  if(document.getElementById('isRemoveWallpaper').checked == true) {
   isRemoveWallpaper = removeWallpaperPrice;  	
   }
  //Штукатурка стен	
  var needWallPlaster = 0;
  if(document.getElementById('needWallPlaster').checked == true) {
   needWallPlaster = wallPlasterPrice+gruntPrice;  
   	
   }
  //Шпаклевка стен     
//   var needWallPutty = 0;
//   if(document.getElementById('needWallPutty').checked == true) {
//    needWallPutty = wallPlasterPrice;          
//         }  	
  	
//Ввыбор финишной оттделки стен  
  var wallFinishType = document.getElementById("wallFinish");//получаем ссылку на элемент Select
  var wallFinishTypeSelected =  parseInt(wallFinish.options[wallFinish.selectedIndex].value);
  
  var wallPutty = 0; //shpaklevka price
  var wallDecoration = 0; // oboi, kraska, etc
  var wallSum = 0;
  
  //вывод подробной инфы
     document.getElementById("calcWallExt").innerHTML = null;
     document.getElementById("calcWallExt").innerHTML = "<p>Площадь: " + this.sq_wall +" </p>";
   //удаление обоев  
     if(isRemoveWallpaper != 0) {
      document.getElementById("calcWallExt").innerHTML += "<p>Удаление старых обоев ("+removeWallpaperPrice+" руб/м&sup2;): " + 
      (this.sq_wall*removeWallpaperPrice).toFixed(0) +" руб.</p>";
     }
     //штукатурка стен
     if(needWallPlaster != 0) {
        document.getElementById("calcWallExt").innerHTML += "<p>Грунтовка или бетоконтакт ("+gruntPrice+" руб/м&sup2;): " + (this.sq_wall * gruntPrice).toFixed(0) +" руб.</p>";
        document.getElementById("calcWallExt").innerHTML += "<p>Штукатурка ("+wallPlasterPrice+" руб/м&sup2;): " + 
        (this.sq_wall*wallPlasterPrice).toFixed(0) +" руб.</p>";
        Wall.plasterThick = parseFloat(document.getElementById('wallPlasterThick').value).toFixed(1)
        Wall.beto_kont += MatConsuption.beto_kont * this.sq_wall
        Wall.rotband += parseInt(MatConsuption.rotband * this.sq_wall * Wall.plasterThick)   
     }
     
     if (document.getElementById('needWallPutty').checked) {
        
      document.getElementById("calcWallExt").innerHTML += "<p>Грунтовка ("+gruntPrice+" руб/м&sup2;): " + (this.sq_wall * gruntPrice).toFixed(0) +" руб.</p>";
      document.getElementById("calcWallExt").innerHTML += "<p>Шпаклевка ("+ wallPuttyForWallpaper +" руб/м&sup2;): "
       + (this.sq_wall * wallPuttyForWallpaper).toFixed(0) +" руб.</p>";
       wallPutty = wallPuttyForWallpaper+gruntPrice;
       Wall.grunt += this.sq_wall * MatConsuption.grunt;
       Wall.lr += parseInt(this.sq_wall * MatConsuption.lr);
     }
     
    switch (wallFinishTypeSelected) {
    case 0 :
     // ceilingCoverPrice = 0
      break
    case 1 :
      //обои
//       if (document.getElementById('needWallPutty').checked) {
         // wallPutty = 0
 //         }
//             wallPutty += wallPuttyForWallpaper+gruntPrice
            wallDecoration = wallPaper + gruntPrice;
            document.getElementById("calcWallExt").innerHTML += "<p>Грунтовка ("+gruntPrice+" руб/м&sup2;): " + (this.sq_wall * gruntPrice).toFixed(0) +" руб.</p>";
            document.getElementById("calcWallExt").innerHTML += "<p>Обои ("+wallPaper+" руб/м&sup2;): " + 
            Math.round(this.sq_wall * wallPaper).toFixed(0) +" руб.</p>";   
            Wall.grunt += this.sq_wall * MatConsuption.grunt;        
      break
    case 2 :
       //покраска + шпаклевка под покр
       if (document.getElementById('needWallPutty').checked) {
          wallPutty += wallPuttyForPaint + gruntPrice;
          wallDecoration = paint + gruntPrice;
          document.getElementById("calcWallExt").innerHTML += "<p>Грунтовка (" + gruntPrice + " руб/м&sup2;): " + (this.sq_wall * gruntPrice).toFixed(0) + " руб.</p>";
          document.getElementById("calcWallExt").innerHTML += "<p>Финишный слой шпаклевки (" + wallPuttyForPaint + " руб/м&sup2;): " +
             (this.sq_wall * wallPuttyForPaint).toFixed(0) + " руб.</p>";
          document.getElementById("calcWallExt").innerHTML += "<p>Грунтовка (" + gruntPrice + " руб/м&sup2;): " + (this.sq_wall * gruntPrice).toFixed(0) + " руб.</p>";
          document.getElementById("calcWallExt").innerHTML += "<p>Покраска (" + paint + " руб/м&sup2;): " + (this.sq_wall * paint).toFixed(0) + " руб.</p>";
          Wall.grunt += this.sq_wall * MatConsuption.grunt * 2;
          Wall.sheetr += this.sq_wall * MatConsuption.sheetr
          Wall.paint += this.sq_wall * MatConsuption.paint
       }
         //Покраска
       else {
           wallPutty = 0;
           wallDecoration = paint + gruntPrice;
           document.getElementById("calcWallExt").innerHTML += "<p>Грунтовка ("+gruntPrice+" руб/м&sup2;): " + (this.sq_wall*gruntPrice).toFixed(0) +" руб.</p>";
           document.getElementById("calcWallExt").innerHTML += "<p>Покраска ("+paint+" руб/м&sup2;): " + (this.sq_wall*paint).toFixed(0) +" руб.</p>";     
           Wall.grunt += this.sq_wall * MatConsuption.grunt
           Wall.paint += this.sq_wall * MatConsuption.paint      
       }
      break
    case 3 :
       //декоративная штукатурка/краска
       if (document.getElementById('needWallPutty').checked) {
          wallPutty = wallPuttyForWallpaper+gruntPrice
          }
            
            wallDecoration = decorativePaint + gruntPrice; 
            document.getElementById("calcWallExt").innerHTML += "<p>Грунтовка ("+gruntPrice+" руб/м&sup2;): " + (this.sq_wall*gruntPrice).toFixed(0) +" руб.</p>";
            document.getElementById("calcWallExt").innerHTML += "<p>Декоративная штукатурка (краска) ("+ 
            decorativePaint+" руб/м&sup2;): " + (this.sq_wall*decorativePaint).toFixed(0) +" руб.</p>";  
            Wall.grunt += this.sq_wall * MatConsuption.grunt;
            Wall.decora += this.sq_wall * MatConsuption.decora;          
      break      
    default :
      wallDecoration = 0
  }
	
   wallSum = (isRemoveWallpaper + needWallPlaster + wallPutty + wallDecoration) *  this.sq_wall;
       getCalcWall.innerHTML = wallSum.toFixed(0);
       
       

  //////////////////////////////////////////////////////
  /////************** ПОЛ   ****************////////////
  ///////////////////////////////////////////////////// 
  
  //Обнуление шаблона
   clear_object(MatAmount);
  //Копирование свойств
   Floor = copy_obj(MatAmount)  
   

       Floor.floor_thick = parseFloat(document.getElementById("levelingThick").value); //Толщина слоя
       Floor.knf_gvl_thick = parseFloat(document.getElementById("superFloorThick").value); //Высота пола Кнауф
       if (isNaN(Floor.knf_gvl_thick)) {
         alert('Высота КНАУФ-суперпол введена некорректно. Пожалуйста, введите правильное значение например: 5.8') 
         document.getElementById("superFloorThick").value = 5.8;   
         Floor.knf_gvl_thick = 5.8;   
       }
       var isRemoveOldFloor = 0;
       if(document.getElementById('isRemoveOldFloor').checked == true) {
    //удаление старого пола
    isRemoveOldFloor = removeOldFloor;  	
       }
   

       var needLeveling = 0;
       if(document.getElementById("needLeveling").checked && document.getElementById("make_floor").checked) {
    //выравнивание пола
    needLeveling = floorLeveling + gruntPrice; 
       }
       
       var needSuperFloor = 0;
       if(document.getElementById("needSuperFloor").checked && document.getElementById("make_floor").checked) {
    //выравнивание пола Knauf супер пол
    needSuperFloor = superFloor + keramzit + paroizol;
       }       


 var needPlinth = 0;
       if(document.getElementById("needPlinth").checked == true) {
    //плинтус * периметр
    needPlinth = floorPlinth * this.perimetr;
       }
       
       var floorFinishType = document.getElementById("floorFinish");
       var floorFinishTypeSelected =  parseInt(floorFinish.options[floorFinish.selectedIndex].value);
       var floorCoverPrice = 0 ;
       
  //Вывод сумм по видам работ
  
       document.getElementById("calcFloorExt").innerHTML = null;
       document.getElementById("calcFloorExt").innerHTML = "<p>Площадь: " + this.square +" м&sup2;, периметр: " + this.perimetr +" м</p>"
       if(isRemoveOldFloor != 0) {
        document.getElementById("calcFloorExt").innerHTML += "<p title=\"Удаление старого пола, стяжки итп\">Удаление старого покрытия ("+ 
        removeOldFloor+" руб/м&sup2;): " + (this.square*removeOldFloor).toFixed(0) +" руб.</p>";
       }   
       if(needLeveling != 0) {
       

//            СТяжка
         if (Floor.floor_thick > 2) {
             
          
             
//  Стяжка с керамзитом по дв цене грунт+слой+слой
            if (Floor.floor_thick > 4) {
//                  alert(Floor.floor_thick)
                //Толщина финишного слоя стяжки
                var floorFinishThick = Floor.floor_thick - 2
                needLeveling += floorLeveling - gruntPrice*2
                //Объем керамзита умноженный на коэф 0.75
                Floor.keramzit += parseInt(floorFinishThick/100 * this.square * 1000*0.75);
                //Остаток высоты стяжки за вычетом объема керамзита
                var height_ostatok = ((Floor.floor_thick/100 * this.square * 1000)  - Floor.keramzit)/1000/this.square*100

                Floor.cement_mix += parseInt(MatConsuption.cement_mix * height_ostatok * this.square);
                
                
                document.getElementById("calcFloorExt").innerHTML += "<p> Стяжка в два слоя с керамзитом ("+needLeveling+" руб/м&sup2;): " + 
                (this.square*needLeveling).toFixed(0) +" руб.</p>";
                
                Floor.grunt += Math.ceil(this.square * MatConsuption.grunt)  
            }
// Стяжка в один слой грунт+слой
            else {
                Floor.cement_mix += parseInt(MatConsuption.cement_mix * Floor.floor_thick * this.square);
                
                document.getElementById("calcFloorExt").innerHTML += "<p> Стяжка пола ("+floorLeveling+" руб/м&sup2;): " + 
                (this.square*floorLeveling).toFixed(0) +" руб.</p>";
                Floor.grunt += Math.ceil(this.square * MatConsuption.grunt)   
            }
         }        
         else {
//          Наливной пол        
         Floor.levelin += parseInt(MatConsuption.levelin * Floor.floor_thick *this.square);
                         document.getElementById("calcFloorExt").innerHTML += "<p> Наливной пол ("+floorLeveling+" руб/м&sup2;): " + 
                (this.square*floorLeveling).toFixed(0) +" руб.</p>";
                Floor.grunt += Math.ceil(this.square * MatConsuption.grunt) 
       }
    }
    //////////////////////////////////     Knauf супер пол    ////////////////////////////////
    // Кнауф-лис - 20мм
    // Гипсокартон 12мм
    // Керамзит - ?
    // Пароизоляция
       if (needSuperFloor != 0) {
          document.getElementById("calcFloorExt").innerHTML += "<p>Пароизоляционная пленка (" + paroizol + " руб/м&sup2;): " +
             (this.square * paroizol).toFixed(0) + " руб.</p>";
          Floor.paroizol += parseInt(this.square * 1.1)

          document.getElementById("calcFloorExt").innerHTML += "<p>Засыпка керамзита (" + keramzit + " руб/м&sup2;): " +
             (this.square * keramzit).toFixed(0) + " руб.</p>";
             var thick_residue = 0; //остаток на подсыпку керамзита
             thick_residue = Floor.knf_gvl_thick - Pack.knf_gvl - Pack.knf_gvl_thick
             
          document.getElementById("calcFloorExt").innerHTML += "<p>КНАУФ-суперпол (" + superFloor + " руб/м&sup2;): " +
             (this.square * superFloor).toFixed(0) + " руб.</p>";
          Floor.knf_gvl += parseInt(this.square * 1.1);
          Floor.gkl += parseInt(this.square * 1.1);
             if (thick_residue > 3) {
               Floor.keramzit += parseInt((this.square * thick_residue * 10)) //литр      
             }
             else {
                alert('Высота слишком мала для КНАУФ-суперпола')
                Floor.knf_gvl = 0;
             }

       }
     
    
       
       switch (floorFinishTypeSelected) {
    case 0 :
      floorCoverPrice = 0
      break
    case 1 :
      floorCoverPrice = laminat //ламинат
      document.getElementById("calcFloorExt").innerHTML += "<p> Ламинат ("+laminat+" руб/м&sup2;): " + 
      (this.square*laminat).toFixed(0) +" руб.</p>";
      break
    case 2 :
      floorCoverPrice = floorTiles + gruntPrice // плитка
      document.getElementById("calcFloorExt").innerHTML += "<p>Грунтовка ("+gruntPrice+" руб/м&sup2;): " + 
      (this.square*gruntPrice).toFixed(0) +" руб.</p>";
           document.getElementById("calcFloorExt").innerHTML += "<p>Плитка ("+floorTiles+" руб/м&sup2;): " + 
           Math.round(this.square*floorTiles).toFixed(0) +" руб.</p>";	   
      break
    case 3 :
      floorCoverPrice = floorFlooring //паркетная доска
           document.getElementById("calcFloorExt").innerHTML += "<p>Паркетная доска ("+floorFlooring+" руб/м&sup2;): " + 
           (this.square * floorFlooring).toFixed(0) +" руб.</p>";		   
      break
    case 4 :
      floorCoverPrice = linoleum //линолеум 
      document.getElementById("calcFloorExt").innerHTML += "<p>Линолеум ("+linoleum+" руб/м&sup2;): " + (this.square * linoleum).toFixed(0) +" руб.</p>";
      break
    default :
      floorCoverPrice = 0
       }
       if(needPlinth != 0) {
        document.getElementById("calcFloorExt").innerHTML += "<p>Плинтус ("+ floorPlinth+" руб/п.м.): " + (this.perimetr * floorPlinth).toFixed(0) +" руб.</p>";
        Floor.plinth += Math.ceil(((this.perimetr - (this.dWidth * this.dSum)) * 1.1 ))
//          alert(Floor.plinth)
       }           
       if(document.getElementById("isFloorTilesDiagonal").checked == true && floorFinishTypeSelected < 4) {
    floorCoverPrice = (floorCoverPrice * 1.2)
    document.getElementById("calcFloorExt").innerHTML += "<p>Укладка по диагонали - коэффициент 1.2 </p>";
       }
       
       var floorSum = ((isRemoveOldFloor + needLeveling + needSuperFloor + floorCoverPrice ) * this.square) + needPlinth;
       document.getElementById("calcFloor").innerHTML = floorSum.toFixed(0);
       
  	 
    /////***************Итого*****************////////////
       document.getElementById('poto').style.display = 'block';
   document.getElementById('ste').style.display = 'block';
   document.getElementById('pol').style.display = 'block';
    this.ceilingSum = ceilingSum;
    this.wallSum = wallSum;
    this.floorSum = floorSum;
   this.allSum = this.ceilingSum + this.wallSum + this.floorSum;
   if (this.allSum == 0) {
       alert('Пожалуйста, выберите тип помещения и вид работ')
   }
   document.getElementById("allSum").innerHTML = this.allSum.toFixed(0);
// 	alert(allSum);

    if (this.ceilingSum === 0) {
       document.getElementById('poto').style.display = 'none';
   }
   if (this.wallSum === 0) {
       document.getElementById('ste').style.display = 'none';       
   }
  if (this.floorSum === 0) {
       document.getElementById('pol').style.display = 'none';       
   }
   
   if (this.allSum != 0 && this.verbose == 1) {
      document.getElementById('priceSum').style.display = 'block';
   }
   

   jQuery('#itogo').val(jQuery("#priceSum").html());
 
 }

var levelin_change = function () {
   if (document.getElementById('needLeveling').checked) {
      document.getElementById('superFloorThickSpan').style.display = 'none';
   }
   else if (document.getElementById('needSuperFloor').checked) {
      document.getElementById('levelingThickSpan').style.display = 'none';
   }
}

