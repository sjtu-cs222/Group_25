import matplotlib.pyplot as plt
from matplotlib.pyplot import savefig
from metropolis_hastings import *
from deciphering_utils import *
import time
#!/usr/bin/python

import sys
from optparse import OptionParser


def main(argv):
   start_time=time.time()
   inputfile = None
   decodefile = None
   parser = OptionParser()

   parser.add_option("-i", "--input", dest="inputfile", 
                     help="input file to train the code on")
   
   parser.add_option("-d", "--decode", dest="decode", 
                     help="file that needs to be decoded")
   
   parser.add_option("-e", "--iters", dest="iterations", 
                     help="number of iterations to run the algorithm for", default=5000)
    
   parser.add_option("-t", "--tolerance", dest="tolerance", 
                     help="percentate acceptance tolerance, before we should stop", default=0.02)
   
   parser.add_option("-p", "--print_every", dest="print_every", 
                     help="number of steps after which diagnostics should be printed", default=500)

   (options, args) = parser.parse_args(argv)

   filename = options.inputfile
   decode = options.decode
   
   if filename is None:
      print("Input file is not specified. Type -h for help.")
      sys.exit(2)

   if decode is None:
      print("Decoding file is not specified. Type -h for help.")
      sys.exit(2)

   char_to_ix, ix_to_char, tr, fr = compute_statistics(filename)
   
   # print(char_to_ix)

   s = list(open(decode, 'r',encoding="utf-8-sig").read())
   # print(len(s))
   scrambled_text = list(s)
   print(len(scrambled_text))
   # thecorrect=open(decode[:-14]+".txt", 'r',encoding="utf-8-sig").read()
   i = 0
   accuricies=[]
   #revision
   # initial_state = get_state(scrambled_text, tr, fr, char_to_ix)
   #revision
   states = []
   entropies = []
   errors=[]
   plt.figure(1)#figsize=(40,30),dpi=80)
   # plt.figure(2)
   while i < 3:
      #revision
      initial_state = get_state(scrambled_text, tr, fr, char_to_ix)
      #revision
      iters = int(options.iterations)
      print_every = int(options.print_every)
      tolerance = options.tolerance
      state, lps, error = metropolis_hastings(initial_state, propose_a_move, compute_probability_of_state, 
                                            iters=iters, print_every=print_every, tolerance=tolerance,error_function=None,pretty_state=pretty_state,theanswer=None)#thecorrect)
      # error_function=compute_error
      # plt.figure(1)
      if(i==0):      
         x=[i for i in range(len(lps))]
         plt.figure(1)
         ax1 = plt.subplot(311)
         plt.plot(x, lps,color = 'red')
         # x=[i for i in range(len(error))]
         # plt.figure(2)
         # ax4 = plt.subplot(311)
         # plt.plot(x, error,color = 'red')
         
      elif(i==1):
         x=[i for i in range(len(lps))]
         plt.figure(1)
         ax2 = plt.subplot(312)
         plt.plot(x, lps,color = 'green')
         # x=[i for i in range(len(error))]
         # plt.figure(2)
         # ax5 = plt.subplot(312)
         # plt.plot(x, error,color = 'green')
      else:
         x=[i for i in range(len(lps))]
         plt.figure(1)
         ax3 = plt.subplot(313)
         plt.plot(x, lps,color = 'blue')
         # x=[i for i in range(len(error))]
         # plt.figure(2)
         # ax6 = plt.subplot(313)
         # plt.plot(x, error,color = 'blue')
         
      
      
      states.extend(state)
      entropies.extend(lps)
      # errors.extend(error)
      i += 1#revision

   
   plt.figure(1)
   ax1.set_title("entropy of 1st,2nd,3rd trial")
   plt.savefig(decode[:-4]+"_entropy.jpg")
   
   # plt.figure(2)
   # plt.savefig(decode[:-4]+"_accuracy.jpg")
   # ax4.set_title("accuracy of 1st,2nd,3rd trial")
   
   # plt.tight_layout()
   plt.show()  

   
   #revision
   p = list(zip(states, entropies))
   p.sort(key=lambda x:x[1])
   
   print("Best Guesses : ")
   
   fout=open(decode[:-4]+"_result.txt", 'w', encoding="utf-8")
   for j in range(1,6):
      print(j,"th","with entropy",-p[-j][1])
      # print(pretty_state(p[-j][0], full=True))
      fout.write(pretty_state(p[-j][0], full=True))
      fout.write("\n\n\n\n")
   fout.close()
   end_time=time.time()
   print("time:",end_time-start_time)
   plt.show()
   
if __name__ == "__main__":
   main(sys.argv)