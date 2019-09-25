function splitCityStateZip() {
 	var address = document.getElementById("id_city").value;

 	var regex_pattern = new RegExp("([A-Z][a-z]+\\s?)+,\\s[A-Z]{2}\\s\\d{5}")
 	var cityStateZip = {
 		error: false
 	};

 	if (regex_pattern.test(address) != true) {
 		cityStateZip.error = true;
 		return cityStateZip;
 	}

	var comma = address.indexOf(',');
	cityStateZip.city = address.slice(0, comma);
	var after = address.substring(comma + 2);
	var space = after.lastIndexOf(' ');
	cityStateZip.state = after.slice(0, space);
	cityStateZip.zip = after.substring(space + 1);
	return cityStateZip;
}

function fillCityStateZip() {
	cityStateZip = splitCityStateZip();
	if (cityStateZip.error != true) {
		document.getElementById("id_city").value = cityStateZip.city;
		document.getElementById("id_state").value = cityStateZip.state;
		document.getElementById("id_zip_code").value = cityStateZip.zip;
	}
}

window.onload = function () { document.getElementById("id_city").onchange = fillCityStateZip }



