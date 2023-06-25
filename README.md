# python_crawling study
<a name="readme-top"></a>
## python 

### 리스트 변수

1. 리스트 선언
```
    - 리스트 변수 =[]
    - 리스트 변수 = list()
    - 리스트변수 = [데이터1, 데이터2 ''']
```
2. 리스트 추가
```
    - 리스트변수.append(data)
    - 리스트변수.insert(indexNum, data)
```
3. 리스트 삭제
```
    - 리스트변수.remove(data)
    - del 리스트변수[인덱스번호]
```
4. 리스트 데이터 수정
```
   리스트변수[인덱스번호] = 수정할 데이터
```

  
### 데이터 구조(List, Tuple, Dictionary, Set)

#### 데이터 구조(Tuple)

##### Tuple은 괄호를 이용해 선언할 수 있다.
  - tuple1 = (1, 2, 3, 4)

##### Tuple은 삭제나 추가가 불가능 하다.
    del tuple[1]
    tuple[1] = 'c'

##### Tuple끼리 더하거나 반복하는 것은 가능하다
- tuple2 = (5, 6) <br>
- print(tuple1 + tuple2) <br>
- print(tuple * 3)

#####  tuple로 변수끼리 값을 편하게 바꿀 수 있다
    x = 2 
    y = 3

    (x, y) = (y, x)

    print('x= ',x,'y = ', y)

#### 데이터 구조 (dictionary의 선언)
    dict1 = 3
    print (dict1)
    
##### dictionary는 key와 value로 이루어져 있고, 추가하는 방법
    dict1 = {'name': 'jahyun'} 
    print (dict1)
    dict1 = ('국어': 55, '수학': 80, '과학': [30, 70, 80, 60])
    print (dict1)
    dict1['영어'] = "pass"
    print (dict1)
##### 요소 삭제는 del을 활용
    del dict1['수학']
    print (dict1)

##### key를 활용해 value를 출력
    print (dict1 ['수학'])

##### key만 출력
    print (dict1.keys())

##### value만 출력할땐 이렇게 합니다.
    print (dict1.values())

##### key와 value를 함께 출력합니다.
    print (dict1.items ())

#### 데이터 구조(set)

##### Set 선언
    
    ppap = {'pen', 'apple', 'pineapple', 'pen'}
    print(ppap)

    'apple' in ppap
    'applepen' in ppap
    
    pineapple = set('pineapple')
    pineapple
    
  A = set('golang')
  B = set('python')
![download](https://github.com/code-hyun/study_python_crawling/assets/122762287/c6ce7111-7143-4107-87bc-d00435ae83c8)

------------------------------------------------------------------------------------------------------------------------------


#### Spring Framework의 장점

	- 프로젝트 전체 구조를 설계할 때 유용하다(빠른 속도로  서버 제작 가능)
	- 다른 프레임워크들의 포용, 여러 프레임워크를 혼용해서 사용 가능하며 이를 접착성이 좋다고 한다.
	- 개발 생산성과 개발도구의 지원


#### Spring Boot

	Spring Framework를 사용함에 있어서 초기 설정 및 필요한 라이브러리에 대한 설정의 어려움이 많으며,
	시간이 너무 오래 걸리 때문에 자동 설정(AutoConfiguration)과 개발에 필요한 모든 것을 관리해주는
	스프링 부트를 선호한다. 각 코어 및 라이브러리의 버전들도 맞추어야 하지만 스프링 부트를 사용하면
	이러한 복잡성을 해결하기에도 좋다.

#### Spring Framework의 특징

	- POJO 기반의 구성
	- DI를 통한 객체간의 관계 구성
	- AOP 지원
	- Transaction 관리
	- 편리한 MVC 구조
	- WAS에 종속적이지 않은 개발 환경


#### ▶ POJO 기반의 구성

	오래된 방식의 간단한 자바 객체라는 의미이며, JAVA코드에서 일반적으로 객체를 구성하는 방식을
	Spring Framework에서 그대로 사용할 수 있다는 의미이다.


#### ▶ 의존성 주입(DI)을 통한 객체간의 관계 구성

	의존성(Dependency)이란 하나의 객체가 다른 객체 없이 제대로 된 역할을 할 수 없다는 것을 의미한다.
	예를 들어 A객체가 B객체 없이 동작이 불가능한 상황을 "A가 B에 의존적이다"라고 표현한다.
	하지만 직접 A필드에 B객체를 선언하면 결합도가 단단해지기 때문에 유연성이 떨어진다.

	주입(Injection)은 외부에서 내부로 밀어 넣는 것을 의미한다.
	필요한 객체를 외부에서 밀어 넣어 유연성을 높이고 결합도를 느슨하게 해준다.
	주입을 받는 입장에서는 어떤 객체인지 신경 쓸 필요가 없고 어떤 객체에 의존하든 자신의 역할은 변하지 않는다.

   	***의존성
   	A →→→→→→→→→→→→→ B
   	A객체에서 B객체를 필드로 직접 생성

	***의존성 주입
	A ↔↔↔↔↔ ? ↔↔↔↔↔ B
	A는 B가 필요하다고 신호를 보내고, ?가 B객체를 외부에서 생성하여 주입하게 된다.
	Spring Framework에서는 ApplicationContext가 ?이며,
	필요한 객체들을 생성 및 주입해주는 역할을 한다. 따라서 개발자들은 기존의 프로그래밍과는 달리
	객체와 객체를 분리해서 생성하고, 이러한 객체를 엮는 wiring 작업의 형태로 개발하게 된다.

	ApplicationContext가 관리하는 객체들을 빈(Bean)이라 부르고,
	빈과 빈 사이의 의존관계를 처리하는 방식으로는 XML, 어노테이션, JAVA 방식이 있다.


#### ▶ AOP의 지원

	관점 지향 프로그래밍.
	좋은 개발 환경에서는 개발자가 비지니스 로직에만 집중할 수 있게 한다.
	Spring Framework는 반복적인 코드를 제거해줌으로써 핵심 비지니스 로직에만
	집중할 수 있는 방법을 제공한다.
	보안이나 로그, 트랜잭션, 예외처리와 같이 비지니스 로직은 아니지만,
	반드시 처리가 필요한 부분을 주변 로직(횡단 관심사)라고 하고, 개발해야할 서비스는 메인 로직(종단 관심사)라고 한다.
	Spring Framwork는 이러한 횡단 관심사를 분리해서 설계하는 것이 가능하고, 횡단 관심사를 모듈로
	분리하는 프로그래밍을 AOP라고 한다.
	핵심 비지니스 로직에만 집중하여 코드 개발이 가능해지고, 각 프로젝트마다 다른 관심사 적용 시 코드 수정을
	최소화 할 수 있으며, 원하는 관심사의 유지보수가 수월한 코드로 구성이 가능해진다.
	※ 비지니스 로직: 서비스를 개발하기 위한 소스코드 및 알고리즘



