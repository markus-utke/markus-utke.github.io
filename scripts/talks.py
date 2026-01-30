#%%

import pandas as pd
from dateutil import parser


# latex cv

df = pd.read_excel('../talks.ods', na_filter="")
output_lines = []

df = df.sort_values("date")

output_lines_invited = []
output_lines_talks = []
output_lines_other = []

last_year = ""
for _, row in reversed(list(df.iterrows())):
    title = row["title"]
    type = row["type"]
    event = row["event"]
    event_short = row["event_short"]
    venue = row["venue"]
    location = row["location"]
    date = row["date"].strftime("%b %Y")
    type_details = row["type_details"]
    
    if type == "Talk" or type == "Poster":
        output_lines_talks.append(
            r"\cventry{" + date + 
            r"}{" + 
            event + ((r" \hbox{(" + event_short + ")}") if event_short else "") +
            r"}{}{" + 
            ((r"\newline " + location ) if location else "") +
            ((r"\newline \textit{" + type_details + r"}") if type_details else "") +
            r"}{}{" + 
            r"Title: \textit{" + title + r"}" +
            r"}"
        )
    elif type == "Invited Talk":
        output_lines_invited.append(
            r"\cventry{" + date + 
            r"}{" + 
            event + ((r" \hbox{(" + event_short + ")}") if event_short else "") +
            r"}{}{" + 
            ((r"\newline " + venue ) if venue else "") +
            ((r"\newline \textit{" + type_details + r"}") if type_details else "") +
            r"}{}{" + 
            r"Title: \textit{" + title + r"}" +
            r"}"
        )
    elif type == "Online Talk":
        output_lines_other.append(
            r"\cventry{" + date + 
            r"}{" + 
            event + (f"({event_short})" if event_short else "") +
            r"}{}{" + 
            ((r"\newline \textit{" + type_details + r"}") if type_details else "") +
            r"}{}{" + 
            r"Title: \textit{" + title + r"}" +
            r"}"
        )
    



latex_output_invited = "\n".join(output_lines_invited)
latex_output_talks = "\n".join(output_lines_talks)
latex_output_other = "\n".join(output_lines_other)

latex_output_other += "\n" + r"\cventry{Jan 2024}{19th Summer School in Discrete Mathematics}{}{\newline Valparaíso, Chile}{}{}"

latex_output = (
    r"\section{Invited talks} " + "\n" + latex_output_invited +"\n\n" + r"\betweenSectionSpace" + "\n\n"
    r"\section{Conference and Workshop Presentations}" + "\n" + latex_output_talks + "\n\n" + r"\betweenSectionSpace" + "\n\n"
    r"\section{Other Attended Events}" + "\n" + latex_output_other +"\n\n" + r"\betweenSectionSpace"
)

print(latex_output)
