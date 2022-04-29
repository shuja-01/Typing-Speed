from time import *
import random as r

def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error += 1
        except:
            error += 1
    return error

def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/ time_R
    return round(speed)

if __name__ == '__main__':
    while True:
        ck = input("Ready to test : yes/no : ")
        if ck == "yes":
            test = ['Nikola Tesla, (born July 9/10, 1856, Smiljan, Austrian Empire [now in Croatia]—died January 7, 1943, New York, New York, U.S.), Serbian American inventor and engineer who discovered and '
                    'patented the rotating magnetic field, the basis of most alternating-current machinery. He also developed the three-phase system of electric power transmission. He immigrated to the United'
                    ' States in 1884 and sold the patent rights to his system of alternating-current dynamos, transformers, and motors to George Westinghouse. In 1891 he invented the Tesla coil, an induction coil'
                    ' widely used in radio technology.',
                    'Thomas Edison, in full Thomas Alva Edison, (born February 11, 1847, Milan, Ohio, U.S.—died October 18, 1931, West Orange, New Jersey), American inventor who, singly or jointly, held a world-record '
                    '1,093 patents. In addition, he created the world’s first industrial research laboratory. Edison was the quintessential American inventor in the era of Yankee ingenuity. He began his career in 1863, '
                    'in the adolescence of the telegraph industry, when virtually the only source of electricity was primitive batteries putting out a low-voltage current. Before he died, in 1931, he had played a '
                    'critical role in introducing the modern age of electricity. From his laboratories and workshops emanated the phonograph, the carbon-button transmitter for the telephone speaker and microphone, the'
                    ' incandescent lamp, a revolutionary generator of unprecedented efficiency, the first commercial electric light and power system, an experimental electric railroad, and key elements of motion-picture '
                    'apparatus, as well as a host of other inventions.',
                    'Aryabhata, also called Aryabhata I or Aryabhata the Elder, (born 476, possibly Ashmaka or Kusumapura, India), astronomer and the earliest Indian mathematician whose work and history are available '
                    'to modern scholars. He is also known as Aryabhata I or Aryabhata the Elder to distinguish him from a 10th-century Indian mathematician of the same name. He flourished in Kusumapura—near Patalipurta '
                    '(Patna), then the capital of the Gupta dynasty—where he composed at least two works, Aryabhatiya (c. 499) and the now lost Aryabhatasiddhanta. Aryabhatasiddhanta circulated mainly in the northwest of '
                    'India and, through the Sāsānian dynasty (224–651) of Iran, had a profound influence on the development of Islamic astronomy. Its contents are preserved to some extent in the works of Varahamihira '
                    '(flourished c. 550), Bhaskara I (flourished c. 629), Brahmagupta (598–c. 665), and others. It is one of the earliest astronomical works to assign the start of each day to midnight.',
                    'Chandrasekhara Venkata Raman was born at Tiruchirappalli in Southern India on November 7th, 1888. His father was a lecturer in mathematics and physics so that from the first he was immersed in an '
                    'academic atmosphere. He entered Presidency College, Madras, in 1902, and in 1904 passed his B.A. examination, winning the first place and the gold medal in physics; in 1907 he gained his M.A. degree,'
                    ' obtaining the highest distinctions.His earliest researches in optics and acoustics – the two fields of investigation to which he has dedicated his entire career – were carried out while he was a student.'
                    'Since at that time a scientific career did not appear to present the best possibilities, Raman joined the Indian Finance Department in 1907; though the duties of his office took most of his time, Raman found '
                    'opportunities for carrying on experimental research in the laboratory of the Indian Association for the Cultivation of Science at Calcutta (of which he became Honorary Secretary in 1919).',
                    'Srinivasa Ramanujan, (born December 22, 1887, Erode, India—died April 26, 1920, Kumbakonam), Indian mathematician whose contributions to the theory of numbers include pioneering discoveries of the properties of'
                    ' the partition function. When he was 15 years old, he obtained a copy of George Shoobridge Carr’s Synopsis of Elementary Results in Pure and Applied Mathematics, 2 vol. (1880–86). This collection of thousands'
                    ' of theorems, many presented with only the briefest of proofs and with no material newer than 1860, aroused his genius. Having verified the results in Carr’s book, Ramanujan went beyond it, developing his'
                    ' own theorems and ideas. In 1903 he secured a scholarship to the University of Madras but lost it the following year because he neglected all other studies in pursuit of mathematics.']



            test1 = r.choice(test)
            print("********Typing speed******** ")
            print(test1)
            print()
            print()
            time_1 = time()
            testinput=input("Enter : ")
            time_2 = time()
            print("Speed :",speed_time(time_1, time_2, testinput), "w/sec")
            print("Error : ",mistake(test1, testinput))

        elif ck == "no":
            break

        else:
            print("Wrong Ipput")

