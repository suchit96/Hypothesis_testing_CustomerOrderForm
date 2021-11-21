

library(readxl)

COF<-read.csv(choose.files())
View(COF)
attach(COF)


?prop.test

table1<- table(COF$Phillippines)
table1
table2<- table(COF$Indonesia)
table2
table3<- table(COF$Malta)
table3
table4<- table(COF$India)
table4
prop.test(x=c(29),n=(271))
# Phillipens p-value=
prop.test(x=c(33),n=(267))
# Indonesia P-value = 0.1235955
prop.test(x=c(31),n=(269))
# Malta P-value = 0.1152416
prop.test(x=c(20),n=(280))

