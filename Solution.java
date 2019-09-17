package SETheoryHomework;


/**
 * @author wjz
 * @date 2019/9/2
 *
 */
public class Solution {
	private int flag = -1;
	private String aroute;
	private String siteIn;
	private String siteOut;
	private String from;
	private String to;
	
	public boolean init(String[] args){
		boolean ret = true;
		int argsLen = args.length;
		switch (argsLen) {
		case 0:
			System.out.println("请输入参数");
			ret = false;
			break;
		case 2:
			this.siteIn = args[1];
			flag = 1;
			break;
		case 6:
			this.aroute = args[1];
			this.siteIn = args[3];
			this.siteOut = args[5];
			flag = 2;
			break;
		case 7:
			this.from = args[1];
			this.to = args[2];
			this.siteIn = args[4];
			this.siteOut = args[6];
			flag = 3;
			break;
		default:
			System.out.println("非法参数，请检查");
			ret = false;
			break;
		}	
		return ret;
	}
	
	
	
	public boolean conditionOne(){
		boolean ret = false;
		//根据每条线路生成线路的Json对象
		
		
		return ret;
	}
	
	public boolean conditionTwo(){
		boolean ret = false;
		
		
		return ret;
	}
	
	public boolean conditionThree(){
		boolean ret = false;
		
		
		return ret;
	}
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		
		Solution s = new Solution();
		if(s.init(args)){
			switch (s.flag) {
			case 1:
				s.conditionOne();
				break;
			case 2:
				s.conditionTwo();
				break;
			case 3:
				s.conditionThree();
				break;
			default:
				return;
			}
		}else {
			return;
		}
	}
}
