
import codecs
content = r'''% !TEX TS-program = luatex
% USA STEM CV LaTeX Template
%
% Author:
% Sabrina Benge
%
% Template license:
% CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
\documentclass[localFont,alternative]{documentMETADATA}
\name{\textbf{ALLYSON HALLEY}}{SOARES DA ROCHA}
\tagline{Arquiteto de Software e Líder Técnico}

\socialinfo{
	\smartphone{+55 081 9 9818 7161}
 \email{allysonhalley@gmail.com}\\
	\address{Olinda, Pernambuco-BRA}
	\github{allysonhalley}\\
	\linkedin{allysonhalley}\\
	\website{https://www.hefti.com.br}{hefti.com.br}
	%\infos{}
}

\begin{document}
	\makecvheader
	\makecvfooter
		{\textsc{}} %\selectlanguage{english}\today
		{\textsc{Allyson Halley - CV}}
		{\thepage}

	\input{section_headline}                % Research Statement
	\input{section_honors_awards}			% Section Honors and Awards
	\input{section_experience}	        	% Section Professional Experience

	\input{section_courses}          % Section Certifications
	\input{section_skills}				    % Section Skills
	\input{section_languages}					% Section languaqes
	
% 	\input{section_interets}				% Section interests
% 	\input{section_projects}                 % Section Projects
% 	\input{section_outreach_volunteering}   % Section Professional Outreach and volunteering
% 	\input{section_teaching_mentoring}      % Section Teaching and Mentoring
% 	\input{section_references} 				% Section references
	


\end{document}
'''
with codecs.open('cv.tex', 'w', encoding='utf-8') as f:
    f.write(content)

