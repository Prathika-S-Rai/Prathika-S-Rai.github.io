package javatrn;
import java.util.*;
public class ATM {
	public static void main(String[] args)
	{
		Machine a=new Machine();
		Thread t1=new Thread(a,"1");
		Thread t2=new Thread(a,"2");
		Thread t3=new Thread(a,"3");
		Thread t4=new Thread(a,"4");
		t1.start();
		t2.start();
		t3.start();
		t4.start();
	}

}
class Machine extends Thread
{
	int amt,bal=12000;
	Scanner sc=new Scanner(System.in);
	public void getAmt()
	{
		System.out.println("Enter the amt");
		amt=sc.nextInt();
		if(amt<bal)
		{
			bal-=amt;System.out.println(amt+" withdrawn");
		}
		else
			System.out.println("Cannot Withdraw");
	}
	synchronized public void run()
	{
		System.out.println(Thread.currentThread().getName()+" "+
		Thread.currentThread().getId()+" "+Thread.currentThread().getPriority());
		getAmt();
	}
}
