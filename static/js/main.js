/*bmi calculation*/

let button = document.getElementById('btn');

button.addEventListener('click', () => {
    const height = parseInt(document.getElementById('height').value);
    const weight = parseInt(document.getElementById('weight').value);
    const result = document.getElementById('output');
    let height_status = false,
        weight_status = false;

    if (height === '' || isNaN(height) || (height <= 0)) {
        document.getElementById('height_error').innerHTML = 'Please provide a valid height';
    } else {
        document.getElementById('height_error').innerHTML = '';
        height_status = true;
    }

    if (weight === '' || isNaN(weight) || (weight <= 0)) {
        document.getElementById('weight_error').innerHTML = 'Please provide a valid weight';
    } else {
        document.getElementById('weight_error').innerHTML = '';
        weight_status = true;
    }

    if (height_status && weight_status) {
        const bmi = (weight / ((height * height) / 10000)).toFixed(2);

        if (bmi < 18.6) {
            result.innerHTML = 'Under weight : ' + bmi;
        } else if (bmi >= 18.6 && bmi < 24.9) {
            result.innerHTML = 'Normal : ' + bmi;
        } else {
            result.innerHTML = 'Over weight : ' + bmi;
        }
    } else {
        alert('The form has errors');
        result.innerHTML = '';
    }
});
/*end bmi calculation*/

/*feet to cm calculate*/
let buttonx = document.getElementById('btnx');

buttonx.addEventListener('click', () => {
    const cm = parseInt(document.getElementById('x').value);
    const resultcm = document.getElementById('outputx');
    if (cm >= 0) {
        const feet = (cm * 12 * 2.54).toFixed(1);
        resultcm.innerHTML = 'Feet To Centemeter : ' + feet;
    } else {
        alert('The form has errors');
        resultcm.innerHTML = '';
    }
});
/*end feet to cm calculate*/

/*Inche to cm calculate*/
let buttony = document.getElementById('btny');

buttony.addEventListener('click', () => {
    const cm2 = parseInt(document.getElementById('y').value);
    const resultcm2 = document.getElementById('outputy');
    if (cm2 >= 0) {
        const inch = (cm2 * 2.54).toFixed(1);
        resultcm2.innerHTML = 'Inche To Centemeter : ' + inch;
    } else {
        alert('The form has errors');
        resultcm2.innerHTML = '';
    }
});
/*end inche to cm calculate*/

/*ideal weight calculate */
let idealbutton = document.getElementById('idealbtn');

idealbutton.addEventListener('click', () => {
    const m2 = parseInt(document.getElementById('idealheight').value);
    const idealresult = document.getElementById('idealoutput');
    if (m2 >= 0) {
        const ideal = (m2 * m2 * 22).toFixed(1);
        if (ideal < 44.5) {
            idealresult.innerHTML = 'Low Body Weight Range: ' + ideal;
        } else if (ideal >= 44.5 && ideal < 60.0) {
            idealresult.innerHTML = 'Ideal Body Weight Range: ' + ideal;
        } else {
            idealresult.innerHTML = 'High Body Weight Range : ' + ideal;
        }

    } else {
        alert('The form has errors');
        idealresult.innerHTML = '';
    }
});
/*end ideal weight calculate*/

/*inch to meter calculation*/
let insconvert = document.getElementById('btnins');

btnins.addEventListener('click', () => {
    const insvalue = parseInt(document.getElementById('ins').value);
    const insresult = document.getElementById('outputins');
    if (insvalue >= 0) {
        const insfinal = (insvalue * 0.0254).toFixed(1);
        insresult.innerHTML = 'Inche To Centemeter : ' + insfinal;
    } else {
        alert('The form has errors');
        insresult.innerHTML = '';
    }
});
/*end inch to meter calculation*/

/*body fat calculation men*/
let buttonp = document.getElementById('btnp');

buttonp.addEventListener('click', () => {
    const weightp = parseInt(document.getElementById('weightp').value);
    const waistp = parseInt(document.getElementById('waistp').value);
    const resultp = document.getElementById('outputp');
    let weightp_status = false,
        waistp_status = false;

    if (weightp === '' || isNaN(weightp) || (weightp <= 0)) {
        document.getElementById('weightp_error').innerHTML = 'Please provide a valid bmi';
    } else {
        document.getElementById('weightp_error').innerHTML = '';
        weightp_status = true;
    }

    if (waistp === '' || isNaN(waistp) || (waistp <= 0)) {
        document.getElementById('waistp_error').innerHTML = 'Please provide a valid age';
    } else {
        document.getElementById('waistp_error').innerHTML = '';
        waistp_status = true;
    }

    if (weightp_status && waistp_status) {
        const x = ((weightp * 1.082) + 94.42).toFixed(1);
        const y = (waistp * 4.15).toFixed(1);
        const z = (x - y);
        const pre = (weightp - z).toFixed(1);;
        const final = ((pre * 100) / weightp).toFixed(1);

        if (final < 18.6) {
            resultp.innerHTML = 'Under weight : ' + final;
        } else
        if (final >= 18.6 && final < 24.9) {
            resultp.innerHTML = 'Normal : ' + final;
        } else {
            resultp.innerHTML = 'Over weight : ' + final;
        }
    } else {
        alert('The form has errors');
        resultp.innerHTML = '';
    }
});
/*end bfp calculation*/

/*start female bfp calculation*/
let buttonpercen = document.getElementById('btnpercen');

buttonpercen.addEventListener('click', () => {
    const we = parseInt(document.getElementById('weightpercen').value);
    const wr = parseInt(document.getElementById('wristpercen').value);
    const wa = parseInt(document.getElementById('waistpercen').value);
    const hi = parseInt(document.getElementById('hippercen').value);
    const fo = parseInt(document.getElementById('forpercen').value);

    const re = document.getElementById('outputpercen');

    if (we >= 0 && wr >= 0 && wa >= 0 && hi >= 0 && fo >= 0) {
        const a = ((we * 0.732) + 8.987).toFixed(1);
        const b = (wr / 3.140).toFixed(1);
        const c = (wa * 0.157).toFixed(1);
        const d = (hi * 0.249).toFixed(1);
        const e = (fo * 0.434).toFixed(1);
        const k = (a + b - c - d + e);
        const m = (we - k).toFixed(1);
        const finalresult = ((m * 100) / we).toFixed(1);
        re.innerHTML = 'final result:' + finalresult;

    } else {
        alert('The form has errors');
        re.innerHTML = '';
    }
});
/*end female*/