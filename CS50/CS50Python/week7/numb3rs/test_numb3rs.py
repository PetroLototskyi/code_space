from numb3rs import validate

def test_digits():
    assert validate (r"cat.dog.pig.rat") == False
    assert validate (r"125.15.83.16") == True
    assert validate (r"!!!.125.# %.~") == False

def test_size():
    assert validate(r"-5.0.125.16") == False
    assert validate(r"5.270.125.16") == False
    assert validate(r"5.70.700.16") == False
    assert validate(r"5.30.125.315") == False
    assert validate(r"5.255.125.16") == True

def test_qty():
    assert validate(r"5.0.125.16.12") == False
    assert validate(r"5.250.125") == False
    assert validate(r"5.70") == False
    assert validate(r"7") == False
    assert validate(r"255.255.255.1") == True

