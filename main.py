from board_dao import *

board_dao = BoardDAO()

while True:
    print("=" * 50)
    print("1.목록  2.등록  3.내용  4.삭제  0.종료")
    print("=" * 50)

    menu = input("선택 > ")

    if menu == "0":
        break

    elif menu == "1":  # 1. 목록 보기
        boards = board_dao.select_all()
        print("\n--- 전체 게시글 목록 ---")
        
        # 💡 [중요] board_dao.py에 select_all()도 이름 형태로 가져오게 맞춰줍니다.
        # 만약 여기서 에러가 나면 아래 '참고' 부분을 봐주세요!
        for board in boards:
            # 이제 숫자가 아닌 이름(key)으로 안전하게 출력합니다.
            # 사용하시는 구조에 따라 아래 형식을 맞춰주세요.
            if isinstance(board, dict):
                print(f"번호: {board['id']} | 제목: {board['title']} | 작성자: {board['writer']} | 조회수: {board['views']} | 날짜: {board['created_at']}")
            else:
                print(f"번호: {board[0]} | 제목: {board[1]} | 작성자: {board[3]} | 조회수: {board[5]} | 날짜: {board[4]}")
        print()

    elif menu == "2":  # 2. 등록하기
        print("\n--- 새 글 등록 ---")
        title = input("제목 입력: ")
        content = input("내용 입력: ")
        writer = input("작성자 입력: ")
        password = input("게시글 비밀번호 설정: ")
        
        board_dao.insert_board(title, content, writer, password)
        print("💡 글이 성공적으로 등록되었습니다!\n")

    elif menu == "3":  # 3. 내용 상세보기
        print("\n--- 글 내용 보기 ---")
        board_id = input("조회할 글 번호(ID) 입력: ")
        
        board = board_dao.select_one(board_id)
        if board:  
            print("-" * 50)
            print(f"글번호: {board['id']} | 조회수: {board['views']}")
            print(f"제목  : {board['title']}")
            print(f"작성자: {board['writer']}")
            print(f"작성일: {board['created_at']}")
            print("-" * 50)
            print(f"내용  :\n{board['content']}")
            print("-" * 50)
        else:
            print("❌ 해당 번호의 게시글이 존재하지 않습니다.\n")

    elif menu == "4":  # 4. 삭제하기
        print("\n--- 글 삭제 ---")
        board_id = input("삭제할 글 번호(ID) 입력: ")
        
        board = board_dao.select_one(board_id)
        if board:
            # 💡 이제 무조건 이 안으로 들어와서 힌트가 뜹니다!
            db_password = str(board['password']).strip() 
            print(f"🔍 [힌트] DB에 저장된 실제 비밀번호: '{db_password}'")
            
            input_password = input("게시글 비밀번호를 입력하세요: ").strip()
            
            if input_password == db_password:
                board_dao.delete_board(board_id)
                print(f"🗑️ {board_id}번 글이 정상적으로 삭제되었습니다.\n")
            else:
                print("❌ 비밀번호가 틀렸습니다. 삭제할 수 없습니다.\n")
        else:
            print("❌ 존재하지 않는 글 번호입니다. 번호를 다시 확인해 주세요.\n")

print("게시판 종료")
