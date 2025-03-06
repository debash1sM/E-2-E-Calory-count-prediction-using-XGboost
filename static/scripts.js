$(document).ready(function() {
    console.log('jQuery is loaded and running!');

    // Function to check if all fields are filled
    function checkFields() {
        let allFilled = true;
        $('form input, form select').each(function() {
            if ($(this).val() === '') {
                allFilled = false;
                return false; // Break out of the loop
            }
        });
        return allFilled;
    }

    // Function to check for unnatural input
    function checkUnnaturalInput() {
        let isValid = true;
        $('.error-message').remove();
        $('input, select').removeClass('error');
        
        const gender = $('#Gender').val();
        const age = parseInt($('#Age').val());
        const height = parseFloat($('#Height').val());
        const weight = parseFloat($('#Weight').val());
        const duration = parseFloat($('#Duration').val());
        const heartRate = parseFloat($('#Heart_Rate').val());
        const bodyTemp = parseFloat($('#Body_Temp').val());
        
        if(gender == -1) { 
            $('#Gender').addClass('error').after('<div class="error-message">Please select gender.</div>');
            isValid = false;
        } 

        if (age <= 0 || age > 120) {
            $('#Age').addClass('error').after('<div class="error-message">Age must be between 1 and 120.</div>');
            isValid = false;
        }
        if (height <= 0 || height > 250) {
            $('#Height').addClass('error').after('<div class="error-message">Height must be between 1 and 250 cm.</div>');
            isValid = false;
        }
        if (weight <= 0 || weight > 150) {
            $('#Weight').addClass('error').after('<div class="error-message">Weight must be between 1 and 150 kg.</div>');
            isValid = false;
        }
        if (duration <= 0 || duration > 240) {
            $('#Duration').addClass('error').after('<div class="error-message">Duration must be between 1 and 240 minutes.</div>');
            isValid = false;
        }
        if (heartRate <= 0 || heartRate > 220) {
            $('#Heart_Rate').addClass('error').after('<div class="error-message">Heart Rate must be between 1 and 220 bpm.</div>');
            isValid = false;
        }
        if (bodyTemp <= 30 || bodyTemp > 45) {
            $('#Body_Temp').addClass('error').after('<div class="error-message">Body Temperature must be between 30 and 45 °C.</div>');
            isValid = false;
        }

        return isValid;
    }

    // Event listener for input and select fields
    $('form input, form select').on('keyup change input', function() {
        if (checkUnnaturalInput() && checkFields()) {
            $('#submit').prop('disabled', false);
        } else {
            $('#submit').prop('disabled', true);
        }
    });

    // Initial check to disable the submit button if fields are not filled
    $('#submit').prop('disabled', !checkFields());
});