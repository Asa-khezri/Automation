function myFunction() {
  var doc = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var values = doc.getDataRange().getValues();
  
  var form = FormApp.create("Name something");
  var formGrid = form.addGridItem();
    formGrid
    .setTitle("Rate your interests")
    .setRows(values[0])
    .setColumns([1, 2, 3, 4, 5]);

  ScriptApp.newTrigger("average")
  .forForm(form.getId())
  .onFormSubmit()
  .create();
  Logger.log(form.getId())
}


function average(){
  var doc = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var values = doc.getDataRange().getValues()[0];
  var formResponses = FormApp.openById("1lY_2TpjOs7JoeEFhV2dIDgkZOHaojRveJCK2gCBjv58").getResponses()

  var sums = []
  var count = [];
  for(var i =0;i<values.length;i++){
  sums.push(0);
  count.push(0)
  }

  for (const element of formResponses) {
    var res = element.getItemResponses();
    for (var j = 0; j < res.length; j++) {
      var item = res[j];
      var scales = item.getResponse();
      for (var k = 0; k < scales.length; k++) {
        if(scales[k]){
        sums[k] += parseInt(scales[k]);
        count[k]+=1;
        //Logger.log(sums[k],count[k])
        }

      }
    }
  }


for (var i = 0; i < values.length; i++) {
  if(count[i])
  doc.getRange(2,i+1).setValue(sums[i] / count[i]);
}




  
}
