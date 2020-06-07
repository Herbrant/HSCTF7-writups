import java.util.Scanner;
public class AscII {
	static int num = 0;
	
	public static void main(String[] args) {
		//  Scanner sc = new Scanner(System.in);
		//  System.out.print("Enter your  guess: ");
		//  String guess = ""
		 
		//  if (guess.length()!= 12) 
		// 	 System.out.println("Sorry, thats wrong.");
		//  else {
		// 	 if(flagTransformed(guess).equals("I$N]=6YiVwC")) 
		// 		 System.out.println("Yup the flag is flag{" + guess + "}");			 
		// 	 else 
		// 		 System.out.println("nope"); 
		//  }

		System.out.println(bruteForce("I$N]=6YiVwC"));
	}

	public static String flagTransformed(String guess) {
		char[] transformed = new char[12];
		
		for(int i = 0; i < 12; i++) {
			num = 1;
			transformed[i] = (char)(((int)guess.charAt(i) + pickNum(i + 1)) % 127);	
		}
		
		char[] temp = new char[12];		
		for(int i = 11; i >= 0; i--) 
			temp[11-i] = transformed[i];
			
		return new String(temp);	
	}
	
	public static char flagTransformed(String guess, int index) {
		char[] transformed = new char[12];
		
		for(int i = 0; i < 12; i++) {
			num = 1;
			transformed[i] = (char)(((int)guess.charAt(i) + pickNum(i + 1)) % 127);	
		}
		
		char[] temp = new char[12];		
		for(int i = 11; i >= 0; i--) 
			temp[11-i] = transformed[i];
			
		return temp[index];	
	}

	public static String bruteForce(String val){
		char[] temp = new char[12];

		for(int i = 0; i < 12; i++)
			temp[i] = (char)(0);

		for(int i = 0; i < 12; i++){
			for(int j = 0; j < 255; j++){
				temp[i] = (char)j;

				String tempString = new String(temp);

				char ch = flagTransformed(tempString, 11-i);

				if(ch == val.charAt(11 - i))
					break;
		
			}
		}

		return new String(temp);
	}
	
	private static int pickNum(int i) {
		
		for(int x = 0; x <= i; x++)
			num+=x;
		
		if(num % 2 == 0)
			return num;
		else 
			num = pickNum(num);
		
		return num;		
	}	 
}