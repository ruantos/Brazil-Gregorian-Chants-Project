import csv
import os
import re


def get_chant_data():
    # This data is pre-compiled from web searches to correct and augment keywords.
    return [
        {'number': '1', 'original_title': '''Accedite ad Dominum''', 'corrected_title': '''Accedite ad Dominum''', 'keywords': {'ad', 'dominum', 'accedite'} },
        {'number': '2', 'original_title': '''Ad Cenam Agni (Tempo Pascal)''', 'corrected_title': '''Ad Cenam Agni (Tempo Pascal)''', 'keywords': {'pascal', 'agni', 'cenam', 'tempo'} },
        {'number': '3', 'original_title': '''Adoremus in aeternum''', 'corrected_title': '''Adoremus in aeternum''', 'keywords': {'aeternum', 'adoremus'} },
        {'number': '4', 'original_title': '''Adoremus in aeternum''', 'corrected_title': '''Adoremus in aeternum''', 'keywords': {'aeternum', 'adoremus'} },
        {'number': '5', 'original_title': '''Adoro te devote''', 'corrected_title': '''Adoro te devote''', 'keywords': {'adoro', 'devote'} },
        {'number': '6', 'original_title': '''Adoro te devote (Ambrosiano)''', 'corrected_title': '''Adoro te devote (Ambrosiano)''', 'keywords': {'adoro', 'devote', 'ambrosiano'} },
        {'number': '7', 'original_title': '''aeterne Rex altissime''', 'corrected_title': '''aeterne Rex altissime''', 'keywords': {'aeterne', 'rex', 'altissime'} },
        {'number': '8', 'original_title': '''Anima Christi''', 'corrected_title': '''Anima Christi''', 'keywords': {'anima', 'christi'} },
        {'number': '9', 'original_title': '''Anima Christi (Ambrosiano)''', 'corrected_title': '''Anima Christi (Ambrosiano)''', 'keywords': {'anima', 'christi', 'ambrosiano'} },
        {'number': '10', 'original_title': '''Anima Christi (Ambrosiano)''', 'corrected_title': '''Anima Christi (Ambrosiano)''', 'keywords': {'anima', 'christi', 'ambrosiano'} },
        {'number': '11', 'original_title': '''Anima Christi... Miserere (Ambrosiano)''', 'corrected_title': '''Anima Christi... Miserere (Ambrosiano)''', 'keywords': {'miserere', 'anima', 'christi', 'ambrosiano'} },
        {'number': '12', 'original_title': '''Ave verum''', 'corrected_title': '''Ave verum''', 'keywords': {'ave', 'verum'} },
        {'number': '13', 'original_title': '''Ave verum (Ambrosiano)''', 'corrected_title': '''Ave verum (Ambrosiano)''', 'keywords': {'ave', 'verum', 'ambrosiano'} },
        {'number': '14', 'original_title': '''Christe, vivens Hostia''', 'corrected_title': '''Christe, vivens Hostia''', 'keywords': {'hostia', 'christe', 'vivens'} },
        {'number': '15', 'original_title': '''Christum Regem''', 'corrected_title': '''Christum Regem''', 'keywords': {'christum', 'regem'} },
        {'number': '16', 'original_title': '''Cor Dulce Jesu (Coração Eucarístico de Jesus)''', 'corrected_title': '''Cor Dulce Jesu (Coração Eucarístico de Jesus)''', 'keywords': {'dulce', 'jesu', 'coração', 'jesus', 'eucarístico'} },
        {'number': '17', 'original_title': '''Ecce Panis Angelorum''', 'corrected_title': '''Ecce Panis Angelorum''', 'keywords': {'ecce', 'panis', 'angelorum'} },
        {'number': '18', 'original_title': '''Ego sum panis''', 'corrected_title': '''Ego sum panis''', 'keywords': {'panis', 'sum', 'ego'} },
        {'number': '19', 'original_title': '''Ego sum panis (Ambrosiano)''', 'corrected_title': '''Ego sum panis (Ambrosiano)''', 'keywords': {'panis', 'sum', 'ego', 'ambrosiano'} },
        {'number': '20', 'original_title': '''Homo quidam''', 'corrected_title': '''Homo quidam''', 'keywords': {'homo', 'quidam'} },
        {'number': '21', 'original_title': '''Homo quidam (Ambrosiano)''', 'corrected_title': '''Homo quidam (Ambrosiano)''', 'keywords': {'homo', 'quidam', 'ambrosiano'} },
        {'number': '22', 'original_title': '''Jesu, autor clementiae (Ss. Coração de Jesus)''', 'corrected_title': '''Jesu, autor clementiae (Ss. Coração de Jesus)''', 'keywords': {'clementiae', 'jesu', 'coração', 'jesus', 'autor'} },
        {'number': '23', 'original_title': '''Jesu, decus angelicum (Ss. Nome de Jesus)''', 'corrected_title': '''Jesu, decus angelicum (Ss. Nome de Jesus)''', 'keywords': {'jesu', 'jesus', 'nome', 'angelicum', 'decus'} },
        {'number': '24', 'original_title': '''Jesu, dulcis amor (Tempo da Paixão)''', 'corrected_title': '''Jesu, dulcis amor (Tempo da Paixão)''', 'keywords': {'jesu', 'amor', 'dulcis', 'tempo', 'paixão'} },
        {'number': '25', 'original_title': '''Jesu, dulcis memoria (Ss. Nome de Jesus)''', 'corrected_title': '''Jesu, dulcis memoria (Ss. Nome de Jesus)''', 'keywords': {'jesu', 'memoria', 'jesus', 'nome', 'dulcis'} },
        {'number': '26', 'original_title': '''Jesu, nostra refectio''', 'corrected_title': '''Jesu, nostra refectio''', 'keywords': {'refectio', 'jesu', 'nostra'} },
        {'number': '27', 'original_title': '''Jesu, Rex admirabilis (Ss. Nome de Jesus)''', 'corrected_title': '''Jesu, Rex admirabilis (Ss. Nome de Jesus)''', 'keywords': {'jesu', 'rex', 'jesus', 'nome', 'admirabilis'} },
        {'number': '28', 'original_title': '''Laetamini unanimi''', 'corrected_title': '''Laetamini unanimi''', 'keywords': {'laetamini', 'unanimi'} },
        {'number': '29', 'original_title': '''O Mysterium ineffabile''', 'corrected_title': '''O Mysterium ineffabile''', 'keywords': {'ineffabile', 'mysterium'} },
        {'number': '30', 'original_title': '''O Panis dulcissime''', 'corrected_title': '''O Panis dulcissime''', 'keywords': {'panis', 'dulcissime'} },
        {'number': '31', 'original_title': '''O quam amabilis''', 'corrected_title': '''O quam amabilis''', 'keywords': {'quam', 'amabilis'} },
        {'number': '32', 'original_title': '''O quam suavis''', 'corrected_title': '''O quam suavis''', 'keywords': {'quam', 'suavis'} },
        {'number': '33', 'original_title': '''O quam suavis (Ambrosiano)''', 'corrected_title': '''O quam suavis (Ambrosiano)''', 'keywords': {'quam', 'suavis', 'ambrosiano'} },
        {'number': '34', 'original_title': '''O sacrum convivium''', 'corrected_title': '''O sacrum convivium''', 'keywords': {'sacrum', 'convivium'} },
        {'number': '35', 'original_title': '''O sacrum convivium (Ambrosiano)''', 'corrected_title': '''O sacrum convivium (Ambrosiano)''', 'keywords': {'sacrum', 'convivium', 'ambrosiano'} },
        {'number': '36', 'original_title': '''Pange Lingua''', 'corrected_title': '''Pange Lingua''', 'keywords': {'pange', 'lingua'} },
        {'number': '37', 'original_title': '''Pange Lingua (Ambrosiano)''', 'corrected_title': '''Pange Lingua (Ambrosiano)''', 'keywords': {'pange', 'lingua', 'ambrosiano'} },
        {'number': '38', 'original_title': '''Pange Lingua (Ambrosiano – melodia antiquior)''', 'corrected_title': '''Pange Lingua (Ambrosiano – melodia antiquior)''', 'keywords': {'pange', 'lingua', 'melodia', 'antiquior', 'ambrosiano'} },
        {'number': '39', 'original_title': '''Quotiescumque (Ambrosiano)''', 'corrected_title': '''Quotiescumque (Ambrosiano)''', 'keywords': {'quotiescumque', 'ambrosiano'} },
        {'number': '40', 'original_title': '''Sacris Solemniis''', 'corrected_title': '''Sacris Solemniis''', 'keywords': {'sacris', 'solemniis'} },
        {'number': '41', 'original_title': '''Sacris solemniis (Alter tonus)''', 'corrected_title': '''Sacris solemniis (Alter tonus)''', 'keywords': {'tonus', 'sacris', 'alter', 'solemniis'} },
        {'number': '42', 'original_title': '''Salutis humanae Sator''', 'corrected_title': '''Salutis humanae Sator''', 'keywords': {'salutis', 'sator', 'humanae'} },
        {'number': '43', 'original_title': '''Salve Lux mundi''', 'corrected_title': '''Salve Lux mundi''', 'keywords': {'lux', 'salve', 'mundi'} },
        {'number': '44', 'original_title': '''Sancti venite''', 'corrected_title': '''Sancti venite''', 'keywords': {'sancti', 'venite'} },
        {'number': '45', 'original_title': '''Totus formosus''', 'corrected_title': '''Totus formosus''', 'keywords': {'totus', 'formosus'} },
        {'number': '46', 'original_title': '''Ubi caritas''', 'corrected_title': '''Ubi caritas''', 'keywords': {'ubi', 'caritas'} },
        {'number': '47', 'original_title': '''Unus panis''', 'corrected_title': '''Unus panis''', 'keywords': {'unus', 'panis'} },
        {'number': '48', 'original_title': '''Verbum supernum''', 'corrected_title': '''Verbum supernum''', 'keywords': {'verbum', 'supernum'} },
        {'number': '49', 'original_title': '''Verbum supernum (Ambrosiano)''', 'corrected_title': '''Verbum supernum (Ambrosiano)''', 'keywords': {'verbum', 'supernum', 'ambrosiano'} },
        {'number': '50', 'original_title': '''Verbum supernum (Ambrosiano)''', 'corrected_title': '''Verbum supernum (Ambrosiano)''', 'keywords': {'verbum', 'supernum', 'ambrosiano'} },
        {'number': '51', 'original_title': '''Ave Maria''', 'corrected_title': '''Ave Maria''', 'keywords': {'ave', 'maria'} },
        {'number': '52', 'original_title': '''Ave Maris Stella''', 'corrected_title': '''Ave Maris Stella''', 'keywords': {'ave', 'stella', 'maris'} },
        {'number': '53', 'original_title': '''Ave Maris Stella (Alter tonus)''', 'corrected_title': '''Ave Maris Stella (Alter tonus)''', 'keywords': {'tonus', 'ave', 'stella', 'alter', 'maris'} },
        {'number': '54', 'original_title': '''Ave Maria... Virgo serena''', 'corrected_title': '''Ave Maria... Virgo serena''', 'keywords': {'ave', 'virgo', 'serena', 'maria'} },
        {'number': '55', 'original_title': '''Concordi laetitia''', 'corrected_title': '''Concordi laetitia''', 'keywords': {'concordi', 'laetitia'} },
        {'number': '56', 'original_title': '''Cum Jubilo''', 'corrected_title': '''Cum Jubilo''', 'keywords': {'cum', 'jubilo'} },
        {'number': '57', 'original_title': '''Dum vitam in Ara (Sete Dores – Ambrosiano)''', 'corrected_title': '''Dum vitam in Ara (Sete Dores – Ambrosiano)''', 'keywords': {'dores', 'ara', 'dum', 'sete', 'vitam', 'ambrosiano'} },
        {'number': '58', 'original_title': '''Flos Carmeli''', 'corrected_title': '''Flos Carmeli''', 'keywords': {'flos', 'carmeli'} },
        {'number': '59', 'original_title': '''Memorare''', 'corrected_title': '''Memorare''', 'keywords': {'memorare'} },
        {'number': '60', 'original_title': '''Mysterium Ecclesiae''', 'corrected_title': '''Mysterium Ecclesiae''', 'keywords': {'mysterium', 'ecclesiae'} },
        {'number': '61', 'original_title': '''O quam amabilis''', 'corrected_title': '''O quam amabilis''', 'keywords': {'quam', 'amabilis'} },
        {'number': '62', 'original_title': '''Omni die dic Mariae''', 'corrected_title': '''Omni die dic Mariae''', 'keywords': {'omni', 'die', 'dic', 'mariae'} },
        {'number': '63', 'original_title': '''O quot undis (Tempo da Paixão)''', 'corrected_title': '''O quot undis (Tempo da Paixão)''', 'keywords': {'quot', 'undis', 'tempo', 'paixão'} },
        {'number': '64', 'original_title': '''Salve Mater''', 'corrected_title': '''Salve Mater''', 'keywords': {'salve', 'mater'} },
        {'number': '65', 'original_title': '''Salve Virgo singularis''', 'corrected_title': '''Salve Virgo singularis''', 'keywords': {'salve', 'virgo', 'singularis'} },
        {'number': '66', 'original_title': '''Sub tuum praesidium''', 'corrected_title': '''Sub tuum praesidium''', 'keywords': {'tuum', 'sub', 'praesidium'} },
        {'number': '67', 'original_title': '''Summae Deus clementiae (Tempo da Paixão)''', 'corrected_title': '''Summae Deus clementiae (Tempo da Paixão)''', 'keywords': {'deus', 'clementiae', 'summae', 'tempo', 'paixão'} },
        {'number': '68', 'original_title': '''Tota Pulchra''', 'corrected_title': '''Tota Pulchra''', 'keywords': {'tota', 'pulchra'} },
        {'number': '69', 'original_title': '''Tota Pulchra (Ambrosiano)''', 'corrected_title': '''Tota Pulchra (Ambrosiano)''', 'keywords': {'tota', 'pulchra', 'ambrosiano'} },
        {'number': '70', 'original_title': '''Verbum bonum (Tempo da Epifania)''', 'corrected_title': '''Verbum bonum (Tempo da Epifania)''', 'keywords': {'verbum', 'bonum', 'tempo', 'epifania'} },
        {'number': '71', 'original_title': '''Virgo Maria''', 'corrected_title': '''Virgo Maria''', 'keywords': {'virgo', 'maria'} },
        {'number': '72', 'original_title': '''Virgo prudentissima''', 'corrected_title': '''Virgo prudentissima''', 'keywords': {'virgo', 'prudentissima'} },
        {'number': '73', 'original_title': '''Antiphonae Majores''', 'corrected_title': '''Antiphonae Majores''', 'keywords': {'antiphonae', 'majores'} },
        {'number': '74', 'original_title': '''Conditor alme siderum (Ambrosiano)''', 'corrected_title': '''Conditor alme siderum (Ambrosiano)''', 'keywords': {'alme', 'conditor', 'siderum', 'ambrosiano'} },
        {'number': '75', 'original_title': '''Creator alme siderum''', 'corrected_title': '''Creator alme siderum''', 'keywords': {'alme', 'creator', 'siderum'} },
        {'number': '76', 'original_title': '''Em clara vox''', 'corrected_title': '''Em clara vox''', 'keywords': {'clara', 'vox'} },
        {'number': '77', 'original_title': '''Kyrie, salve''', 'corrected_title': '''Kyrie, salve''', 'keywords': {'kyrie', 'salve'} },
        {'number': '78', 'original_title': '''Rorate Caeli''', 'corrected_title': '''Rorate Caeli''', 'keywords': {'caeli', 'rorate'} },
        {'number': '79', 'original_title': '''Rorate Caeli (Ambrosiano)''', 'corrected_title': '''Rorate Caeli (Ambrosiano)''', 'keywords': {'caeli', 'rorate', 'ambrosiano'} },
        {'number': '80', 'original_title': '''Veni, Redemptor gentium''', 'corrected_title': '''Veni, Redemptor gentium''', 'keywords': {'veni', 'gentium', 'redemptor'} },
        {'number': '81', 'original_title': '''Veni, veni Emmanuel''', 'corrected_title': '''Veni, veni Emmanuel''', 'keywords': {'veni', 'emmanuel'} },
        {'number': '82', 'original_title': '''Verbum supernum... a Patre''', 'corrected_title': '''Verbum supernum... a Patre''', 'keywords': {'verbum', 'patre', 'supernum'} },
        {'number': '83', 'original_title': '''A solis ortus''', 'corrected_title': '''A solis ortus''', 'keywords': {'solis', 'ortus'} },
        {'number': '84', 'original_title': '''Candor aeterne''', 'corrected_title': '''Candor aeterne''', 'keywords': {'aeterne', 'candor'} },
        {'number': '85', 'original_title': '''Christe Redemptor omnium''', 'corrected_title': '''Christe Redemptor omnium''', 'keywords': {'christe', 'omnium', 'redemptor'} },
        {'number': '86', 'original_title': '''Christus natus est''', 'corrected_title': '''Christus natus est''', 'keywords': {'est', 'natus', 'christus'} },
        {'number': '87', 'original_title': '''Ecce nomen Domini''', 'corrected_title': '''Ecce nomen Domini''', 'keywords': {'ecce', 'nomen', 'domini'} },
        {'number': '88', 'original_title': '''Intende qui regis (Ambrosiano)''', 'corrected_title': '''Intende qui regis (Ambrosiano)''', 'keywords': {'intende', 'regis', 'qui', 'ambrosiano'} },
        {'number': '89', 'original_title': '''Jesu Redemptor omnium''', 'corrected_title': '''Jesu Redemptor omnium''', 'keywords': {'jesu', 'omnium', 'redemptor'} },
        {'number': '90', 'original_title': '''Laetabundus''', 'corrected_title': '''Laetabundus''', 'keywords': {'laetabundus'} },
        {'number': '91', 'original_title': '''Puer natus''', 'corrected_title': '''Puer natus''', 'keywords': {'puer', 'natus'} },
        {'number': '92', 'original_title': '''Resonet in laudibus''', 'corrected_title': '''Resonet in laudibus''', 'keywords': {'laudibus', 'resonet'} },
        {'number': '93', 'original_title': '''Crudelis Herodes''', 'corrected_title': '''Crudelis Herodes''', 'keywords': {'crudelis', 'herodes'} },
        {'number': '94', 'original_title': '''Crudelis Herodes (Alter tonus)''', 'corrected_title': '''Crudelis Herodes (Alter tonus)''', 'keywords': {'tonus', 'herodes', 'alter', 'crudelis'} },
        {'number': '95', 'original_title': '''Epiphaniam Domino''', 'corrected_title': '''Epiphaniam Domino''', 'keywords': {'domino', 'epiphaniam'} },
        {'number': '96', 'original_title': '''Herodis insanus furor (Ambrosiano)''', 'corrected_title': '''Herodis insanus furor (Ambrosiano)''', 'keywords': {'furor', 'herodis', 'insanus', 'ambrosiano'} },
        {'number': '97', 'original_title': '''Illuminans, Altissime (Ambrosiano)''', 'corrected_title': '''Illuminans, Altissime (Ambrosiano)''', 'keywords': {'altissime', 'illuminans', 'ambrosiano'} },
        {'number': '98', 'original_title': '''Magi videntes''', 'corrected_title': '''Magi videntes''', 'keywords': {'magi', 'videntes'} },
        {'number': '99', 'original_title': '''O sola magnarum''', 'corrected_title': '''O sola magnarum''', 'keywords': {'sola', 'magnarum'} },
        {'number': '100', 'original_title': '''Quicumque Christus''', 'corrected_title': '''Quicumque Christus''', 'keywords': {'quicumque', 'christus'} },
        {'number': '101', 'original_title': '''Attende Domine''', 'corrected_title': '''Attende Domine''', 'keywords': {'domine', 'attende'} },
        {'number': '102', 'original_title': '''Audi benigne Conditor''', 'corrected_title': '''Audi benigne Conditor''', 'keywords': {'audi', 'conditor', 'benigne'} },
        {'number': '103', 'original_title': '''Audi benigne Conditor (Ambrosiano)''', 'corrected_title': '''Audi benigne Conditor (Ambrosiano)''', 'keywords': {'audi', 'conditor', 'benigne', 'ambrosiano'} },
        {'number': '104', 'original_title': '''Christe qui lux''', 'corrected_title': '''Christe qui lux''', 'keywords': {'lux', 'christe', 'qui'} },
        {'number': '105', 'original_title': '''Ex more docti (Ambrosiano)''', 'corrected_title': '''Ex more docti (Ambrosiano)''', 'keywords': {'more', 'docti', 'ambrosiano'} },
        {'number': '106', 'original_title': '''Exite Sion''', 'corrected_title': '''Exite Sion''', 'keywords': {'sion', 'exite'} },
        {'number': '107', 'original_title': '''Gloriam sacrae''', 'corrected_title': '''Gloriam sacrae''', 'keywords': {'sacrae', 'gloriam'} },
        {'number': '108', 'original_title': '''Jesu, quadragenariae''', 'corrected_title': '''Jesu, quadragenariae''', 'keywords': {'jesu', 'quadragenariae'} },
        {'number': '109', 'original_title': '''Lux alma, Christe (Ambrosiano)''', 'corrected_title': '''Lux alma, Christe (Ambrosiano)''', 'keywords': {'lux', 'christe', 'alma', 'ambrosiano'} },
        {'number': '110', 'original_title': '''Media vita''', 'corrected_title': '''Media vita''', 'keywords': {'media', 'vita'} },
        {'number': '111', 'original_title': '''Miserere et parce''', 'corrected_title': 'Miserere et parce', 'keywords': {'parce', 'miserere'} },
        {'number': '112', 'original_title': '''O Caput cruentatum''', 'corrected_title': '''O Caput cruentatum''', 'keywords': {'caput', 'cruentatum'} },
        {'number': '113', 'original_title': '''O sol salutis''', 'corrected_title': '''O sol salutis''', 'keywords': {'sol', 'salutis'} },
        {'number': '114', 'original_title': '''Parce Domine''', 'corrected_title': '''Parce Domine''', 'keywords': {'domine', 'parce'} },
        {'number': '115', 'original_title': '''Precemur omnes''', 'corrected_title': '''Precemur omnes''', 'keywords': {'precemur', 'omnes'} },
        {'number': '116', 'original_title': '''Quaenam lingua tibi''', 'corrected_title': '''Quaenam lingua tibi''', 'keywords': {'tibi', 'quaenam', 'lingua'} },
        {'number': '117', 'original_title': '''Hymnum canamus (Para a Quinta-feira Santa – Ambrosiano)''', 'corrected_title': '''Hymnum canamus (Para a Quinta-feira Santa – Ambrosiano)''', 'keywords': {'feira', 'santa', 'para', 'quinta', 'hymnum', 'canamus', 'ambrosiano'} },
        {'number': '118', 'original_title': '''Kyrie''', 'corrected_title': '''Kyrie''', 'keywords': {'kyrie'} },
        {'number': '119', 'original_title': '''O Crux benedicta (Ambrosiano)''', 'corrected_title': '''O Crux benedicta (Ambrosiano)''', 'keywords': {'crux', 'benedicta', 'ambrosiano'} },
        {'number': '120', 'original_title': '''O Crux splendidior''', 'corrected_title': '''O Crux splendidior''', 'keywords': {'crux', 'splendidior'} },
        {'number': '121', 'original_title': '''Salve Crux Sancta''', 'corrected_title': '''Salve Crux Sancta''', 'keywords': {'crux', 'salve', 'sancta'} },
        {'number': '122', 'original_title': '''Vexilla Regis''', 'corrected_title': '''Vexilla Regis''', 'keywords': {'regis', 'vexilla'} },
        {'number': '123', 'original_title': '''Vexilla Regis (Ambrosiano)''', 'corrected_title': '''Vexilla Regis (Ambrosiano)''', 'keywords': {'regis', 'vexilla', 'ambrosiano'} },
        {'number': '124', 'original_title': '''Ad regias Agni dapes''', 'corrected_title': '''Ad regias Agni dapes''', 'keywords': {'ad', 'agni', 'dapes', 'regias'} },
        {'number': '125', 'original_title': '''Ad regias Agni dapes (Alter tonus)''', 'corrected_title': '''Ad regias Agni dapes (Alter tonus)''', 'keywords': {'tonus', 'ad', 'agni', 'dapes', 'alter', 'regias'} },
        {'number': '126', 'original_title': '''Chorus novus Jerusalem''', 'corrected_title': '''Chorus novus Jerusalem''', 'keywords': {'novus', 'chorus', 'jerusalem'} },
        {'number': '127', 'original_title': '''Christus resurrexit''', 'corrected_title': '''Christus resurrexit''', 'keywords': {'resurrexit', 'christus'} },
        {'number': '128', 'original_title': '''Ego sum Alpha''', 'corrected_title': '''Ego sum Alpha''', 'keywords': {'sum', 'alpha', 'ego'} },
        {'number': '129', 'original_title': '''Exsultemus et laetemur''', 'corrected_title': '''Exsultemus et laetemur''', 'keywords': {'exsultemus', 'laetemur'} },
        {'number': '130', 'original_title': '''Hic est dies (Ambrosiano)''', 'corrected_title': '''Hic est dies (Ambrosiano)''', 'keywords': {'est', 'hic', 'dies', 'ambrosiano'} },
        {'number': '131', 'original_title': '''Laetare, caelum''', 'corrected_title': '''Laetare, caelum''', 'keywords': {'caelum', 'laetare'} },
        {'number': '132', 'original_title': '''Lux et origo''', 'corrected_title': '''Lux et origo''', 'keywords': {'lux', 'origo'} },
        {'number': '133', 'original_title': '''O filii et filiae''', 'corrected_title': '''O filii et filiae''', 'keywords': {'filii', 'filiae'} },
        {'number': '134', 'original_title': '''O Rex aeterne''', 'corrected_title': '''O Rex aeterne''', 'keywords': {'rex', 'aeterne'} },
        {'number': '135', 'original_title': '''Rex sempiterne cœlitum''', 'corrected_title': '''Rex sempiterne cœlitum''', 'keywords': {'rex', 'sempiterne', 'cœlitum'} },
        {'number': '136', 'original_title': '''Salve festa dies''', 'corrected_title': '''Salve festa dies''', 'keywords': {'salve', 'festa', 'dies'} },
        {'number': '137', 'original_title': '''Optatus votis omnium''', 'corrected_title': '''Optatus votis omnium''', 'keywords': {'omnium', 'optatus', 'votis'} },
        {'number': '138', 'original_title': '''Optatus orbis gaudio (Ambrosiano)''', 'corrected_title': '''Optatus orbis gaudio (Ambrosiano)''', 'keywords': {'orbis', 'optatus', 'gaudio', 'ambrosiano'} },
        {'number': '139', 'original_title': '''Beata nobis gaudia''', 'corrected_title': '''Beata nobis gaudia''', 'keywords': {'beata', 'nobis', 'gaudia'} },
        {'number': '140', 'original_title': '''Jam Christus astra''', 'corrected_title': '''Jam Christus astra''', 'keywords': {'jam', 'astra', 'christus'} },
        {'number': '141', 'original_title': '''Jam Christus astra (Ambrosiano)''', 'corrected_title': '''Jam Christus astra (Ambrosiano)''', 'keywords': {'jam', 'astra', 'christus', 'ambrosiano'} },
        {'number': '142', 'original_title': '''Veni, Creator''', 'corrected_title': '''Veni, Creator''', 'keywords': {'veni', 'creator'} },
        {'number': '143', 'original_title': '''Veni, Sancte Spiritus''', 'corrected_title': '''Veni, Sancte Spiritus''', 'keywords': {'sancte', 'veni', 'spiritus'} },
        {'number': '144', 'original_title': '''Adesto, Sancta Trinitas''', 'corrected_title': '''Adesto, Sancta Trinitas''', 'keywords': {'sancta', 'adesto', 'trinitas'} },
        {'number': '145', 'original_title': '''Imensa et Una''', 'corrected_title': '''Imensa et Una''', 'keywords': {'una', 'imensa'} },
        {'number': '146', 'original_title': '''Kyrie, fons bonitatis''', 'corrected_title': '''Kyrie, fons bonitatis''', 'keywords': {'kyrie', 'fons', 'bonitatis'} },
        {'number': '147', 'original_title': '''Te Patrem summum''', 'corrected_title': '''Te Patrem summum''', 'keywords': {'patrem', 'summum'} },
        {'number': '148', 'original_title': '''Auctor beate saeculi''', 'corrected_title': '''Auctor beate saeculi''', 'keywords': {'saeculi', 'auctor', 'beate'} },
        {'number': '149', 'original_title': '''Cor arca legem''', 'corrected_title': '''Cor arca legem''', 'keywords': {'arca', 'legem', 'cor'} },
        {'number': '150', 'original_title': '''Cor Jesu, caritatis''', 'corrected_title': '''Cor Jesu, caritatis''', 'keywords': {'jesu', 'caritatis', 'cor'} },
        {'number': '151', 'original_title': '''Em ut superba''', 'corrected_title': '''Em ut superba''', 'keywords': {'superba'} },
        {'number': '152', 'original_title': '''Jesu, autor clementiae''', 'corrected_title': '''Jesu, autor clementiae''', 'keywords': {'clementiae', 'jesu', 'autor'} },
        {'number': '153', 'original_title': '''Lux alma, Jesu''', 'corrected_title': '''Lux alma, Jesu''', 'keywords': {'lux', 'jesu', 'alma'} },
        {'number': '154', 'original_title': '''Summi Parentis''', 'corrected_title': '''Summi Parentis''', 'keywords': {'summi', 'parentis'} },
        {'number': '155', 'original_title': '''Festivis resonent''', 'corrected_title': '''Festivis resonent''', 'keywords': {'festivis', 'resonent'} },
        {'number': '156', 'original_title': '''Salvete Christi vulnera''', 'corrected_title': '''Salvete Christi vulnera''', 'keywords': {'christi', 'vulnera', 'salvete'} },
        {'number': '157', 'original_title': '''Plaude, Mater caritatis (Ambrosiano)''', 'corrected_title': '''Plaude, Mater caritatis (Ambrosiano)''', 'keywords': {'mater', 'caritatis', 'plaude', 'ambrosiano'} },
        {'number': '158', 'original_title': '''Quicumque Christum quaeritis''', 'corrected_title': '''Quicumque Christum quaeritis''', 'keywords': {'quicumque', 'christum', 'quaeritis'} },
        {'number': '159', 'original_title': '''aeterna imago Altissimus''', 'corrected_title': '''aeterna imago Altissimus''', 'keywords': {'imago', 'aeterna', 'altissimus'} },
        {'number': '160', 'original_title': '''Christus vincit (Ambrosiano)''', 'corrected_title': '''Christus vincit (Ambrosiano)''', 'keywords': {'vincit', 'christus', 'ambrosiano'} },
        {'number': '161', 'original_title': '''Te saeculorum Principem''', 'corrected_title': '''Te saeculorum Principem''', 'keywords': {'principem', 'saeculorum'} },
        {'number': '162', 'original_title': '''Te saeculorum Principem (Ambrosiano)''', 'corrected_title': '''Te saeculorum Principem (Ambrosiano)''', 'keywords': {'principem', 'saeculorum', 'ambrosiano'} },
        {'number': '163', 'original_title': '''Vexilla Christus''', 'corrected_title': '''Vexilla Christus''', 'keywords': {'vexilla', 'christus'} },
        {'number': '164', 'original_title': '''O gente felix (Ambrosiano)''', 'corrected_title': '''O gente felix (Ambrosiano)''', 'keywords': {'gente', 'felix', 'ambrosiano'} },
        {'number': '165', 'original_title': '''O lux beata caelitum''', 'corrected_title': '''O lux beata caelitum''', 'keywords': {'lux', 'beata', 'caelitum'} },
        {'number': '166', 'original_title': '''aeterne rerum Conditor''', 'corrected_title': '''aeterne rerum Conditor''', 'keywords': {'rerum', 'conditor', 'aeterne'} },
        {'number': '167', 'original_title': '''aeterne rerum Conditor (Ambrosiano)''', 'corrected_title': '''aeterne rerum Conditor (Ambrosiano)''', 'keywords': {'rerum', 'conditor', 'aeterne', 'ambrosiano'} },
        {'number': '168', 'original_title': '''Deus, Creator omnium''', 'corrected_title': '''Deus, Creator omnium''', 'keywords': {'deus', 'creator', 'omnium'} },
        {'number': '169', 'original_title': '''Deus, Creator omnium (Ambrosiano)''', 'corrected_title': '''Deus, Creator omnium (Ambrosiano)''', 'keywords': {'deus', 'creator', 'omnium', 'ambrosiano'} },
        {'number': '170', 'original_title': '''Kyrie, Rex aeterno''', 'corrected_title': '''Kyrie, Rex aeterno''', 'keywords': {'rex', 'kyrie', 'aeterno'} },
        {'number': '171', 'original_title': '''Lucis creator optime''', 'corrected_title': '''Lucis creator optime''', 'keywords': {'lucis', 'creator', 'optime'} },
        {'number': '172', 'original_title': '''Lucis creator optime (Alter tonus)''', 'corrected_title': '''Lucis creator optime (Alter tonus)''', 'keywords': {'tonus', 'lucis', 'creator', 'optime', 'alter'} },
        {'number': '173', 'original_title': '''Orbis factor''', 'corrected_title': '''Orbis factor''', 'keywords': {'orbis', 'factor'} },
        {'number': '174', 'original_title': '''Quando Deus (Ao fim do ano litúrgico)''', 'corrected_title': '''Quando Deus (Ao fim do ano litúrgico)''', 'keywords': {'ano', 'deus', 'fim', 'litúrgico', 'quando'} },
        {'number': '175', 'original_title': '''Rerum, Deus, fons''', 'corrected_title': '''Rerum, Deus, fons''', 'keywords': {'deus', 'rerum', 'fons'} },
        {'number': '176', 'original_title': '''Splendor paternae gloriae''', 'corrected_title': '''Splendor paternae gloriae''', 'keywords': {'splendor', 'gloriae', 'paternae'} },
        {'number': '177', 'original_title': '''Dignum canentes Angeli (Ambrosiano)''', 'corrected_title': '''Dignum canentes Angeli (Ambrosiano)''', 'keywords': {'dignum', 'angeli', 'canentes', 'ambrosiano'} },
        {'number': '178', 'original_title': '''Iste Confessor''', 'corrected_title': '''Iste Confessor''', 'keywords': {'iste', 'confessor'} },
        {'number': '179', 'original_title': '''Laudemus Deum nostrum''', 'corrected_title': '''Laudemus Deum nostrum''', 'keywords': {'deum', 'nostrum', 'laudemus'} },
        {'number': '180', 'original_title': '''Te Joseph celebrent''', 'corrected_title': '''Te Joseph celebrent''', 'keywords': {'joseph', 'celebrent'} },
        {'number': '181', 'original_title': '''Ut queant laxis''', 'corrected_title': '''Ut queant laxis''', 'keywords': {'queant', 'laxis'} },
        {'number': '182', 'original_title': '''Nostrae salutis Nunctio''', 'corrected_title': '''Nostrae salutis Nunctio''', 'keywords': {'salutis', 'nostrae', 'nunctio'} },
        {'number': '183', 'original_title': '''Placare Christus servulis''', 'corrected_title': '''Placare Christus servulis''', 'keywords': {'placare', 'servulis', 'christus'} },
        {'number': '184', 'original_title': '''Deo fruentes fulgidae (Ambrosiano)''', 'corrected_title': '''Deo fruentes fulgidae (Ambrosiano)''', 'keywords': {'deo', 'fulgidae', 'fruentes', 'ambrosiano'} },
        {'number': '185', 'original_title': '''Credo quod Redemptor''', 'corrected_title': '''Credo quod Redemptor''', 'keywords': {'quod', 'credo', 'redemptor'} },
        {'number': '186', 'original_title': '''In paradisum''', 'corrected_title': '''In paradisum''', 'keywords': {'paradisum'} },
        {'number': '187', 'original_title': '''Spes, Christe''', 'corrected_title': '''Spes, Christe''', 'keywords': {'spes', 'christe'} },
    ]


def sanitize_filename_from_title(name):
    name = re.sub(r'<.*?>', '', name).strip()
    name = re.sub(r'[\/*?:"<>|]',"", name)
    name = name.replace(" ", "_")
    return name

def get_keywords(title):
    title = re.sub(r'\(.*?\)', '', title)
    words = re.findall(r'\b\w+\b', title.lower())
    return {word for word in words if len(word) > 2}

def find_all_matches(chant_info, all_chants):
    list_keywords = chant_info['keywords']
    if not list_keywords:
        return []

    matches = []
    for chant in all_chants:
        db_keywords = get_keywords(chant['titulo'])
        if not db_keywords:
            continue

        score = len(list_keywords.intersection(db_keywords))
        if list_keywords.issubset(db_keywords):
            score += 5

        if score > 1:
            matches.append((score, chant))
    
    matches.sort(key=lambda x: x[0], reverse=True)
    return [chant for score, chant in matches]

def copy_file(src, dest):
    try:
        with open(src, 'rb') as f_src:
            with open(dest, 'wb') as f_dest:
                f_dest.write(f_src.read())
        return True
    except FileNotFoundError:
        return False

def main():
    try:
        with open('chants.csv', 'r', newline='', encoding='utf-8') as f:
            all_chants = list(csv.DictReader(f))
    except FileNotFoundError:
        print("Erro: O arquivo chants.csv não foi encontrado. Execute o script de busca primeiro.")
        return

    output_csv_path = 'laudate_dominum/laudate_dominum.csv'
    with open(output_csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['numero_lista', 'titulo_lista', 'titulo_corrigido', 'id_gregobase', 'titulo_encontrado'])

        # This uses the pre-compiled data for now.
        # A full implementation would need to parse the raw list first.
        chant_data = get_chant_data()
        processed_titles = {}

        for item in chant_data:
            title_key = item['corrected_title']
            if title_key not in processed_titles:
                processed_titles[title_key] = find_all_matches(item, all_chants)
            
            if processed_titles[title_key]:
                match = processed_titles[title_key].pop(0)
            else:
                match = None

            if match:
                print(f"Encontrado para '{item['original_title']}': ID {match['id']}, Título '{match['titulo']}'")
                writer.writerow([item['number'], item['original_title'], item['corrected_title'], match['id'], match['titulo']])

                sanitized_title = sanitize_filename_from_title(match['titulo'])
                sanitized_version = sanitize_filename_from_title(match['version'])
                filename_base = f"{sanitized_title}-{sanitized_version}" if sanitized_version else sanitized_title
                
                dest_gabc = f"laudate_dominum/gabc/{item['number']}_{filename_base}.gabc"
                dest_pdf = f"laudate_dominum/pdf/{item['number']}_{filename_base}.pdf"

                src_gabc = f"gabc/{filename_base}.gabc"
                if not copy_file(src_gabc, dest_gabc):
                    print(f"  - Arquivo GABC não encontrado: {src_gabc}")

                src_pdf = f"pdf/{filename_base}.pdf"
                if not copy_file(src_pdf, dest_pdf):
                    print(f"  - Arquivo PDF não encontrado: {src_pdf}")
            else:
                print(f"Não foi encontrada correspondência para '{item['original_title']}'")
                writer.writerow([item['number'], item['original_title'], item['corrected_title'], 'NAO ENCONTRADO', 'NAO ENCONTRADO'])

if __name__ == "__main__":
    main()
