////////////////////////////////////
////     Расход материалов     /////
////////////////////////////////////

MatConsuption = {
   rotband : 8.5,   // Ротбанд (гипсовая штукатурка) 	8,5 кг/м2 	10мм
   lr : 1.3,        // Ветонит ЛР+ (шпаклевка) 	1,2 кг/м2 	1мм
   sheetr : 0.374,  // Шитрок (финишная шпаклевка) 	 0,674 кг/м2 	1мм
   cement_mix : 20, // Сухая смесь (цементно-песчаная) 	20 кг/м2 	10мм
   levelin : 16,    // Наливной пол (Старатели) 	16 кг/м2 	10мм
   beto_kont : 0.3, // Бетоконтакт 	0,25 -0,35 кг/м2 
   grunt : 0.1,     // Грунтовка 	0,07–0,1 кг/м2
   paint:   0.17,    // Duluxe 13 m²/L плюс два слоя мин = 0.2L на 1m²
   keramzit : 50,   // Подсыпка под КНФ пол 50 л/м2  при толщине 5см
   knf_gvl : 0.72,   // КНАУФ-суперпол — элемент пола 1200х600х20 мм 
   decora : 0.25,   // Murs de Agat 0.25 L/m2
}


////////////////////////////////////
////    Количесто материалов   /////
////////////////////////////////////

MatAmount = {
   rotband: 0,   // Ротбанд (гипсовая штукатурка) 	8,5 кг/м2 	10мм
   lr: 0,        // Ветонит ЛР+ (шпаклевка) 	1,2 кг/м2 	1мм
   sheetr: 0,    // Шитрок (финишная шпаклевка) 	 0,674 кг/м2 	1мм
   cement_mix: 0,// Сухая смесь (цементно-песчаная) 	20 кг/м2 	10мм
   levelin: 0,   // Наливной пол (Старатели) 	16 кг/м2 	10мм
   beto_kont: 0, // Бетоконтакт 	0,25 -0,35 кг/м2 
   grunt: 0,     // Грунтовка 	0,07–0,1 кг/м2
   gkl: 0,       // Гипсокартон
   keramzit: 0,  // Подсыпка под КНФ пол 50 л/м2  при толщине 5см
   knf_gvl: 0,   // КНАУФ-суперпол — элемент пола 1200х600х20 мм 
   galtel: 0,    //Потолочный плинтус (галтель)
   plinth: 0,    // Плинтус
   paint: 0,     //Водоэмульс краска
   plasterThick : 0, //толщина штукатурки (см)
   decora : 0,       //Декоративная краска
   paroizol : 0,     //пароизоляция под кнауф супер-пол
   floor_thick : 0,  //Толщина стяжки
   knf_gvl_thick : 0, //Высота пола Кнауф
   
}

////////////////////////////////////////////////////
///  Строки для печати, копия ключей MatAmount  ////
////////////////////////////////////////////////////
MatAssoc = {
   rotband: 'Гипсовая штукатурка <strong>ROTBAND</strong> (мешок 30кг): ',   // Ротбанд (гипсовая штукатурка)       8,5 кг/м2       10мм
   lr: 'Шпаклевка <strong>Vetonit LR+</strong> (мешок 20кг): ',        // Ветонит ЛР+ (шпаклевка)     1,2 кг/м2       1мм
   sheetr: 'Шпаклевка финиш. (<strong>Rotband Pasta, Sheetrock</strong>) (кг): ',    // Шитрок (финишная шпаклевка)          0,674 кг/м2    1мм
   cement_mix: "Сухая смесь (цементно-песчаная) (мешок 30 кг): ",// Сухая смесь (цементно-песчаная)     20 кг/м2        10мм
   levelin: 'Наливной пол (<strong>"Старатели"</strong>) (мешок 25кг): ',   // Наливной пол (Старатели)    16 кг/м2        10мм
   beto_kont: 'Бетоконтакт (кг): ', // Бетоконтакт         0,25 -0,35 кг/м2 
   grunt: 'Грунтовка (<strong>Knauf Tiefengrund, Ceresit</strong>)(л): ',     // Грунтовка   0,07–0,1 кг/м2
   gkl: 'Гипсокартон (лист 2500х1200 мм): ',       // Гипсокартон
   keramzit: 'Керамзит (л): ',  // Подсыпка под КНФ пол 50 л/м2  при толщине 5см
   knf_gvl: '<strong>КНАУФ-суперпол</strong> — элемент пола (лист 1200х600х20 мм): ',   // КНАУФ-суперпол — элемент пола 1200х600х20 мм 
   galtel: 'Потолочный плинтус (галтель) (длина 2 м)(шт.):',    //Потолочный плинтус (галтель)
   plinth: 'Плинтус (длина 2.5 м)(шт.): ',    // Плинтус
   paint: 'Водоэмульсионная краска  (<strong>Tikkurila, Beckers </strong>)(л): ',     //Водоэмульс краска
   plasterThick : 'Слой штукатурки (см): ', //толщина штукатурки (см)
   decora : 'Декоративная краска (например <strong>Murs De Agat</strong>) (л): ', //Декоративная краска
   paroizol : 'Пароизоляционная пленка (м2): ',     //пароизоляция под кнауф супер-пол
   floor_thick : 'Высота стяжки (см): ',  //Толщина стяжки
   knf_gvl_thick : 'Высота КНАУФ супер-пола (см): ', //Высота пола Кнауф
}

/****************************************************/
/* Массы мешков смесей, площади листов ГВЛ, ГКЛ итп */
/****************************************************/
Pack = {
   rotband : 30 ,     //масса мешка ротбанда
   lr : 20 ,         //"LR+" kg
   cement_mix : 30,   //масса мешка смеси
   levelin : 25,      //масса мешка наливнорго пола
   galtel : 2,        //потолочный плинтус -2m
   plinth : 2.5,      //длина одного плинтуса
   gkl : 3,           //Площадь листа гипсокартона m2
   gkl_thick : 1.2,   //толщина листа гипсокартоена см
   knf_gvl : 0.72,    // КНАУФ-суперпол - m2
   knf_gvl_thick : 2  // толщина листа Кнауф-супол

}


Ceiling = {} //Потолок
Wall = {}   //Стены
Floor = {}  // Пол

var copy_obj = function(obj) {
   var copy = {};
   for (var key in obj) {
      copy[key] = obj[key];
   }
   return copy;
};



gkl = {
   gkl : 0,
   ppn : 0,
   pp : 0,
   pn2 : 0,
   krab : 0,

}

var clear_object = function (obj) {
      //Обнулить все элементы MatAmount
   for (x in obj) {
      obj[x] = 0;
   } 
   
}

///////////////////////////////////////////
///     Вывод расхода материалов    ///////
///////////////////////////////////////////

amount_format = function (id, amount, square, perimetr) {
         id_ext = id + "Ext"; // куда писать результат
         p_string = ''
         if (perimetr) {
            p_string =  "периметр: " + perimetr +" м"
         }
         document.getElementById(id).innerHTML = "";
         document.getElementById(id + 'Div').style.display = 'block';
         document.getElementById(id_ext).innerHTML = "<p>Площадь: " + square +" м&sup2;, "+ p_string + "</p>"

         var am_format = function (assoc, am) {
             
         //Добавить проверку типа
         return   assoc  + '<span class="showAmount"> ' + am  +   '</span></p>';    
         }
         
         var fine_amount = '';  //Округление расхода
         for (a in amount) {
             if (amount[a] > 0) {
               fine_amount = amount[a];
               if (a in Pack && a != 'knf_gvl_thick') {
                  fine_amount = Math.ceil(amount[a] /Pack[a]);
               }
               else if (a == 'knf_gvl_thick' && document.getElementById('needLeveling').checked){
                  fine_amount = parseFloat(amount[a]);
                  continue
               }
               else if (a == 'floor_thick' && document.getElementById('needSuperFloor').checked ){
                  fine_amount = parseFloat(amount[a]);
                  continue
               }
               else {
                  fine_amount = Math.ceil(parseFloat(amount[a]));               
               }            
               document.getElementById(id_ext).innerHTML += am_format(MatAssoc[a], fine_amount);
               MatAmount[a] += fine_amount;
             }
         }         
}

print_amount = function() {
   //Скрывает все слои
   document.getElementById('matSum').style.display = 'none';
   document.getElementById('matCeilingDiv').style.display = 'none';
   document.getElementById('matWallDiv').style.display = 'none';
   document.getElementById('matFloorDiv').style.display = 'none';

   moneyCalc.calculateAll(0);
   if (moneyCalc.allSum > 0) {
       clear_object(MatAmount);
      document.getElementById('matSum').style.display = 'block';
      if (moneyCalc.ceilingSum > 0) {
         amount_format('matCeiling', Ceiling, moneyCalc.square, moneyCalc.perimetr)
      }
      if (moneyCalc.wallSum > 0) {
         amount_format('matWall', Wall, moneyCalc.sq_wall)
      }
      if (moneyCalc.floorSum > 0) {
         amount_format('matFloor', Floor, moneyCalc.square, moneyCalc.perimetr)
      }
      if (moneyCalc.allSum > 0) {
       document.getElementById('to_sender').style.display = 'block';
      }

      
// Заполнение "Всего по материалам"  - #matAmountAllExt
document.getElementById('matAmountAllExt').innerHTML ='';
   for (k in MatAmount) {
      if (MatAmount[k] > 0) {
      document.getElementById('matAmountAllExt').innerHTML += MatAssoc[k] + '<span class="showAmount"> ' + MatAmount[k] + '</span></p>';
        }
   }

   //      Заполнение формы подробного расхода      
      jQuery('#amount').val(jQuery("#matSum").html());   

//      Заполнение формы общего расхода JSON
//       full_mat = JSON.stringify(MatAmount, null, 2);
//       jQuery('#materials').val(full_mat);

   } else {
//        alert('Пожалуйста, выберите тип помещения и вид работ')
   }
}
//convert objects to JSON
// var full_mat = JSON.stringify(MatAmount, null, 2);
// var assoc = JSON.stringify(MatAssoc, null, 2);


jQuery(document).ready(function($){
   var delay = 300;
    $('#needCeilingPlaster').click(function(){
        $('#ceilingPlasterThickSpan').toggle(delay);
    });
    $('#needWallPlaster').click(function(){
        $('#wallPlasterThickSpan').toggle(delay);
    });
    $('#needLeveling').click(function(){
        $('#levelingThickSpan').toggle(delay);
    });
    $('#needSuperFloor').click(function(){
        $('#superFloorThickSpan').toggle(delay);
    }); 
    $('#make_floor').click(function(){
        $('#make_floor_div').toggle(delay);
    });     
    //заполнение форм    
//     $('#assoc').val(assoc);
    
    //отправка
    var send = function(){
        $('#to_sender').submit();
        alert('sending')
    }
    


});

var to_sender = function() {
    var login = document.getElementById('name').value;
    var mail = document.getElementById('mail').value;
    jQuery('#to_sender').submit();

    
}
///////////////////////////
//TODO Если стяжка толще столько-то см, ОБОИ
////////////////////////////
