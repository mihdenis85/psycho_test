def fun(answers):
    res1 = 0
    res2 = 0
    res3 = 0
    res4 = 0
    res5 = 0
    res6 = 0
    for number in range(len(answers)):
        if number + 1 == 1 and answers[number]: res1 += 1
        if number + 1 == 2 and answers[number]: res1 += 1
        if number + 1 == 3 and answers[number]: res1 += 1
        if number + 1 == 4 and answers[number]: res1 += 1
        if number + 1 == 5 and answers[number]: res1 += 1
        if number + 1 == 16 and answers[number]: res1 += 1
        if number + 1 == 17 and answers[number]: res1 += 1
        if number + 1 == 19 and answers[number]: res1 += 1
        if number + 1 == 21 and answers[number]: res1 += 1
        if number + 1 == 28 and answers[number]: res1 += 1
        if number + 1 == 31 and answers[number]: res1 += 1
        if number + 1 == 32 and answers[number]: res1 += 1
        if number + 1 == 33 and answers[number]: res1 += 1
        if number + 1 == 34 and answers[number]: res1 += 1

        if number + 1 == 1 and not answers[number]: res2 += 1
        if number + 1 == 6 and answers[number]: res2 += 1
        if number + 1 == 7 and answers[number]: res2 += 1
        if number + 1 == 8 and answers[number]: res2 += 1
        if number + 1 == 9 and answers[number]: res2 += 1
        if number + 1 == 16 and not answers[number]: res2 += 1
        if number + 1 == 20 and answers[number]: res2 += 1
        if number + 1 == 22 and answers[number]: res2 += 1
        if number + 1 == 23 and answers[number]: res2 += 1
        if number + 1 == 24 and answers[number]: res2 += 1
        if number + 1 == 31 and not answers[number]: res2 += 1
        if number + 1 == 35 and answers[number]: res2 += 1
        if number + 1 == 36 and answers[number]: res2 += 1
        if number + 1 == 37 and answers[number]: res2 += 1

        if number + 1 == 2 and not answers[number]: res3 += 1
        if number + 1 == 6 and not answers[number]: res3 += 1
        if number + 1 == 10 and answers[number]: res3 += 1
        if number + 1 == 11 and answers[number]: res3 += 1
        if number + 1 == 12 and answers[number]: res3 += 1
        if number + 1 == 17 and not answers[number]: res3 += 1
        if number + 1 == 20 and not answers[number]: res3 += 1
        if number + 1 == 25 and answers[number]: res3 += 1
        if number + 1 == 26 and answers[number]: res3 += 1
        if number + 1 == 27 and answers[number]: res3 += 1
        if number + 1 == 36 and not answers[number]: res3 += 1
        if number + 1 == 38 and answers[number]: res3 += 1
        if number + 1 == 39 and answers[number]: res3 += 1
        if number + 1 == 41 and not answers[number]: res3 += 1

        if number + 1 == 3 and not answers[number]: res4 += 1
        if number + 1 == 7 and not answers[number]: res4 += 1
        if number + 1 == 10 and not answers[number]: res4 += 1
        if number + 1 == 13 and answers[number]: res4 += 1
        if number + 1 == 14 and answers[number]: res4 += 1
        if number + 1 == 18 and answers[number]: res4 += 1
        if number + 1 == 19 and not answers[number]: res4 += 1
        if number + 1 == 22 and not answers[number]: res4 += 1
        if number + 1 == 29 and answers[number]: res4 += 1
        if number + 1 == 32 and not answers[number]: res4 += 1
        if number + 1 == 35 and not answers[number]: res4 += 1
        if number + 1 == 38 and not answers[number]: res4 += 1
        if number + 1 == 40 and answers[number]: res4 += 1
        if number + 1 == 42 and answers[number]: res4 += 1

        if number + 1 == 4 and not answers[number]: res5 += 1
        if number + 1 == 8 and not answers[number]: res5 += 1
        if number + 1 == 11 and not answers[number]: res5 += 1
        if number + 1 == 13 and not answers[number]: res5 += 1
        if number + 1 == 15 and answers[number]: res5 += 1
        if number + 1 == 18 and not answers[number]: res5 += 1
        if number + 1 == 23 and not answers[number]: res5 += 1
        if number + 1 == 25 and not answers[number]: res5 += 1
        if number + 1 == 26 and not answers[number]: res5 += 1
        if number + 1 == 28 and not answers[number]: res5 += 1
        if number + 1 == 30 and answers[number]: res5 += 1
        if number + 1 == 33 and not answers[number]: res5 += 1
        if number + 1 == 39 and not answers[number]: res5 += 1
        if number + 1 == 40 and not answers[number]: res5 += 1

        if number + 1 == 5 and not answers[number]: res6 += 1
        if number + 1 == 9 and not answers[number]: res6 += 1
        if number + 1 == 12 and not answers[number]: res6 += 1
        if number + 1 == 14 and not answers[number]: res6 += 1
        if number + 1 == 15 and not answers[number]: res6 += 1
        if number + 1 == 21 and not answers[number]: res6 += 1
        if number + 1 == 24 and not answers[number]: res6 += 1
        if number + 1 == 27 and not answers[number]: res6 += 1
        if number + 1 == 29 and not answers[number]: res6 += 1
        if number + 1 == 30 and not answers[number]: res6 += 1
        if number + 1 == 34 and not answers[number]: res6 += 1
        if number + 1 == 37 and not answers[number]: res6 += 1
        if number + 1 == 41 and answers[number]: res6 += 1
        if number + 1 == 42 and not answers[number]: res6 += 1

        if max(res1, res2, res3, res4, res5, res6) == res1:
            return "Реалистический – предпочитает работать с вещами, а не с людьми. Это несоциальный, эмоционально-стабильный тип. Ориентирован на настоящее, определенное. Занимается конкретными объектами и их использованием (вещи, инструменты, техника). Хорошо приспосабливается к обстановке, пластичен, трудолюбив. В структуре способностей преобладает невербальные, то есть математические. Люди, относящиеся к этому типу, предпочитают выполнять работу, требующую силы, ловкости, подвижности, хорошей координации движений, навыков практической работы. Результаты труда профессионалов этого типа ощутимы и реальны – их руками создан весь окружающий нас предметный мир. Люди реалистического типа охотнее делают, чем говорят, они настойчивы и уверены в себе, в работе предпочитают четкие и конкретные указания. Придерживаются традиционных ценностей, поэтому критически относятся к новым идеям. Предпочитает занятия требующие конкретности, четкости (оператор ПК, техник, шофер, ювелир, автомеханик, фермер инженер и др.).Близкие типы: интеллектуальный и конвенциальный.Противоположный тип: социальный."
        elif max(res1, res2, res3, res4, res5, res6) == res2:
            return "Интеллектуальный (исследовательский) – ориентирован на труд с идеями и с вещами (объектами). Присуща как пластичность, так и ригидность в действиях. Характеризуется как любознательный, методичный (система в работе), любит работать в одиночку. Отличается целеустремленностью, настойчивостью, терпеливостью. Предпочитает изыскательные профессии (узнать, распознать). Людей, относящихся к этому типу, отличают аналитические способности, рационализм, независимость и оригинальность мышления, умение точно формулировать и излагать свои мысли, решать логические задачи, генерировать новые идеи. Они часто выбирают научную и исследовательскую работу. Им нужна свобода для творчества. Работа способна увлечь их настолько, что стирается грань между рабочим временем и досугом. Мир идей для них может быть важнее, чем общение с людьми. Материальное благополучие для них обычно не на первом месте. Рекомендуемые профессии - метеоролог, научный работник, автор научно - популярных книг и статей, физик, химик, хирург, биолог и др.)Близкие типы: реалистический и артистический.Противоположный тип: предприимчивый."
        elif max(res1, res2, res3, res4, res5, res6) == res3:
            return "Социальный – ориентирован на общение, взаимодействие с другими людьми. Нуждается в контактах, не терпит уединение. Предпочитает работать с людьми, а не с вещами. Ответственен, терпелив, эмпатичен. Развитые вербальные способности, повышенная приспособляемость «пластичность» к меняющейся обстановке. Профессии (сферы деятельности) – обучение, лечение, обслуживание и т.д. Люди, относящиеся к этому типу, предпочитают профессиональную деятельность, связанную с обучением, воспитанием, лечением, консультированием, обслуживанием. Люди этого типа гуманны, чувствительны, активны, ориентированы на социальные нормы, способны понять эмоциональное состояние другого человека. Для них характерно хорошее речевое развитие, живая мимика, интерес к людям, готовность прийти на помощь. Материальное благополучие для них обычно не на первом месте. Рекомендуемые профессии: учитель, преподаватель, психолог, логопед, священнослужитель, врач, продавец др.)"
        elif max(res1, res2, res3, res4, res5, res6) == res4:
            return "Конвенциальный – отдает предпочтение четко структурированной деятельности. Выбирает такие цели и задачи, которые четко подтверждаются обществом и обычаями. Связан с традиционными видами деятельности – канцелярскими, конторскими. Подход к чему-либо – практичен, стереотипен, он не оригинален. Характерны консерватизм, ригидность, но обладает хорошими навыками общения, а также моторными навыками. Настойчив, практичен, дисциплинирован, добросовестен. Преобладают невербальные способности, прекрасный исполнитель. Люди этого типа обычно проявляют склонность к работе, связанной с обработкой и систематизацией информации, предоставленной в виде условных знаков, цифр, формул, текстов (ведение документации, установление количественных соотношений между числами и условными знаками). Они отличаются аккуратностью, пунктуальностью, практичностью, ориентированы на социальные нормы, предпочитают четко регламентированную работу. Материальное благополучие для них более значимо, чем для других типов. Склонны к работе, не связанной с широкими контактами и принятием ответственных решений. Рекомендуемые профессии: экономист, кассир в банке, налоговый инспектор, ревизор, оператор ЭВМ, судебный исполнитель, архивариус, бухгалтер, нотариус, библиотекарь и др.Близкие типы: реалистический и предприимчивый."
        elif max(res1, res2, res3, res4, res5, res6) == res5:
            return "Предприимчивый – выбирает цели и задачи, которые позволяют ему проявить энергию, энтузиазм. Сочетаются импульсивность и холодный расчет. Наделен как вербальными, так и невербальными способностями, обладает интуицией и навыками эффективного межличностного взаимодействия. Интересуется различными сферами жизни и деятельности. Предпочитает работать с людьми и идеями. Самоуверен, тщеславен, склонен к авантюризму. Настойчив в достижении цели, лабилен. Типы темпераментов – холеристический и сангвиник. Люди этого типа находчивы, практичны, быстро ориентируются в сложной обстановке, склонны к самостоятельному принятию решений, социально активны, готовы рисковать, ищут острые ощущения. Любят и умеют общаться. Имеют высокий уровень притязаний. Избегают занятий, требующих усидчивости, большой и длительной концентрации внимания. Для них значимо материальное благополучие. Предпочитают деятельность, требующую энергии, организаторских способностей, связанную с руководством, управлением и влиянием на людей. Рекомендуемые профессии: руководитель, директор, судья, адвокат, брокер, предприниматель, риэлтор и др.Близкие типы: конвенциальный и социальный. Противоположный тип: исследовательский."
        elif max(res1, res2, res3, res4, res5, res6) == res6:
            return "Артистический – сложный взгляд на жизнь, гибкость и независимость в принятии решений. Часто свойственен фатализм. Очень чувствителен, не социален, оригинален. Имеет богатое воображение, склонности к творческой деятельности, обладает хорошей интуицией, независим, эмоционален. Предпочитает занятия творческого характера. Преобладают вербальные способности. Для этого типа характерны исключительные способности восприятия и моторики, высокая чувствительность всех анализаторов. Имеет высокий жизненный идеал, нетривиален. Люди этого типа оригинальны, независимы в принятии решений, редко ориентируются на социальные нормы и одобрение, обладают необычным взглядом на жизнь, гибкостью мышления, эмоциональной чувствительностью. Отношения с людьми строят, опираясь на свои ощущения, эмоции, воображение, интуицию. Они не выносят жесткой регламентации, предпочитая свободный график работы. Часто выбирают профессии, связанные с литературой, театром, кино, музыкой, изобразительным искусством (писатель, фотограф, музыкант, художник, певец, журналист, архитектор, актер, дизайнер).Близкие типы: интеллектуальный и социальный.Противоположный тип: конвенциальный."

