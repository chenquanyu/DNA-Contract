Cversion = '2.0.0'
from DNA.libont import str, hex


def Main():
    a = 12345678987654321
    s_a = str(a)
    assert(s_a == '12345678987654321')

    a = 9797589374729374982374981794371294719827439827491793749173491784712
    s_a = str(a)
    assert(s_a == '9797589374729374982374981794371294719827439827491793749173491784712')

    a = 1378937591759175934898096347592347591789571970179179010971947
    s_a = str(a)
    assert(s_a == '1378937591759175934898096347592347591789571970179179010971947')

    a = 13789375917591759348980963475923475917895719701791790109719477
    s_a = str(a)
    assert(s_a == '13789375917591759348980963475923475917895719701791790109719477')

    a = 137893759175917593489809634759234759178957197017917901097194777
    s_a = str(a)
    assert(s_a == '137893759175917593489809634759234759178957197017917901097194777')

    a = 1378937591759175934898096347592347591789571970179179010971947777
    s_a = str(a)
    assert(s_a == '1378937591759175934898096347592347591789571970179179010971947777')

    a = 13789375917591759348980963475923475917895719701791790109719477777
    s_a = str(a)
    assert(s_a == '13789375917591759348980963475923475917895719701791790109719477777')

    a = 137893759175917593489809634759234759178957197017917901097194777777
    s_a = str(a)
    assert(s_a == '137893759175917593489809634759234759178957197017917901097194777777')

    a = 1378937591759175934898096347592347591789571970179179010971947777777
    s_a = str(a)
    assert(s_a == '1378937591759175934898096347592347591789571970179179010971947777777')

    a = 13789375917591759348980963475923475917895719701791790109719477777777
    s_a = str(a)
    assert(s_a == '13789375917591759348980963475923475917895719701791790109719477777777')

    a = 137893759175917593489809634759234759178957197017917901097194777777777
    s_a = str(a)
    assert(s_a == '137893759175917593489809634759234759178957197017917901097194777777777')

    a = 1378937591759175934898096347592347591789571970179179010971947777777777
    s_a = str(a)
    assert(s_a == '1378937591759175934898096347592347591789571970179179010971947777777777')

    a = 13789375917591759348980963475923475917895719701791790109719477777777777
    s_a = str(a)
    assert(s_a == '13789375917591759348980963475923475917895719701791790109719477777777777')

    a = 13789375917591759348980963475923475917895719701791790109719477777777777777
    s_a = str(a)
    assert(s_a == '13789375917591759348980963475923475917895719701791790109719477777777777777')

    a = 137893759175917593489809634759234759178957197017917901097194777777777777777
    s_a = str(a)
    assert(s_a == '137893759175917593489809634759234759178957197017917901097194777777777777777')

    a = 1378937591759175934898096347592347591789571970179179010971947777777777777777
    s_a = str(a)
    assert(s_a == '1378937591759175934898096347592347591789571970179179010971947777777777777777')

    a = 13789375917591759348980963475923475917895719701791790109719477777777777777777
    s_a = str(a)
    assert(s_a == '13789375917591759348980963475923475917895719701791790109719477777777777777777')

    a = 0x123456789abcdef
    s_a = hex(a)
    assert(s_a == '0x123456789abcdef')

    a = 0x1234567890abcdef0123456789abcdef0123456789abcdef0123456789abcdef
    s_a = hex(a)
    assert(s_a == '0x1234567890abcdef0123456789abcdef0123456789abcdef0123456789abcdef')

    print(s_a)
