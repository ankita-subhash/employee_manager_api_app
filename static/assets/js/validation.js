$('#datepicker').datepicker({
     uiLibrary: 'bootstrap3.3.0'
});
	

function getAge() {
var dateString = document.getElementById("datepicker").value;
if(dateString !="")
{
    var today = new Date();
    var birthDate = new Date(dateString);
    var age = today.getFullYear() - birthDate.getFullYear();
    var m = today.getMonth() - birthDate.getMonth();
    var da = today.getDate() - birthDate.getDate();
    if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
        age--;
    }
    if(m<0){
        m +=12;
    }
    if(da<0){
        da +=30;
    }
    
  if(age < 18 || age > 100)
{
document.getElementById('ra_communication').style.display='block';

} else {

document.getElementById('ra_communication').style.display='none';
}
} else {
document.getElementById('ra_communication').style.display='none';
}
}



function nameCard() {
  var x = document.getElementById("fname");
  x.value = x.value.toUpperCase();
  var x = document.getElementById("mname");
  x.value = x.value.toUpperCase();
  var x = document.getElementById("lname");
  x.value = x.value.toUpperCase();
  var x = document.getElementById("pan_nameoncard");
  x.value = x.value.toUpperCase();
  var x = document.getElementById("ffname");
  x.value = x.value.toUpperCase();
  var x = document.getElementById("fmname");
  x.value = x.value.toUpperCase();
  var x = document.getElementById("flname");
  x.value = x.value.toUpperCase();
  var x = document.getElementById("rhouse");
  x.value = x.value.toUpperCase();
  var x = document.getElementById("rarea");
  x.value = x.value.toUpperCase();
  var x = document.getElementById("rcity");
  x.value = x.value.toUpperCase();
  var x = document.getElementById("pannumber");
  x.value = x.value.toUpperCase();
   var x = document.getElementById("noffice");
  x.value = x.value.toUpperCase();
  var x = document.getElementById("ohouse");
  x.value = x.value.toUpperCase();
  var x = document.getElementById("oarea");
  x.value = x.value.toUpperCase();
  var x = document.getElementById("ocity");
  x.value = x.value.toUpperCase();
  var x = document.getElementById("gfname");
  x.value = x.value.toUpperCase();
  var x = document.getElementById("gmname");
  x.value = x.value.toUpperCase();
  var x = document.getElementById("glname");
  x.value = x.value.toUpperCase();
  var x = document.getElementById("ghouse");
  x.value = x.value.toUpperCase();
  var x = document.getElementById("garea");
  x.value = x.value.toUpperCase();
  var x = document.getElementById("pannumber");
  x.value = x.value.toUpperCase();
  var x = document.getElementById("gcity");
  x.value = x.value.toUpperCase();
}


function show3()
{
	
	document.getElementById('office_communication').style.display='none';
}
function show4()
{
	
	document.getElementById('office_communication').style.display='block';
}


function show5()
{
	document.getElementById('residence_communication').style.display='block';
	document.getElementById('office_communication').style.display='none';
}
function show6()
{
	document.getElementById('residence_communication').style.display='none';
	document.getElementById('office_communication').style.display='block';
}



