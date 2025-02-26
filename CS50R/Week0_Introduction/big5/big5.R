big <- read.table(
  "tests.tsv",
  header = TRUE,
  sep = '\t'
)
big$gender <- factor(
  big$gender,
  labels = c("Unanswered", "Male", "Female", "Other")
)
big$extroversion <- round((big$E1 +big$E2 + big$E3)/15, digits = 2)
big$neuroticism <- round((big$N1 +big$N2 + big$N3)/15, digits = 2)
big$agreeableness <- round((big$A1 +big$A2 + big$A3)/15, digits = 2)
big$conscientiousness <- round((big$C1 +big$C2 + big$C3)/15, digits = 2)
big$openness <- round((big$O1 +big$O2 + big$O3)/15, digits = 2)

write.csv(
  big,
  "analysis.csv",
  row.names = FALSE
)