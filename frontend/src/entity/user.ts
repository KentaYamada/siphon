/**
 * User entity
 */
export default class User {
    public id: number;
    public name: string;
    public nickname: string;
    public email: string;
    public password: string;

    constructor(
        id: number,
        name: string,
        nickname: string,
        email: string,
        password: string) {
        this.id = id;
        this.name = name;
        this.nickname = nickname;
        this.email = email;
        this.password = password;
    }

    public static getDummyUsers(): User[] {
        let list = [];

        for (let i = 1; i < 20; i++) {
            list.push(new User(
                i,
                `User ${i}`,
                `Nickname ${i}`,
                `user${i}.email.com`,
                'test'
            ));
        }

        return list;
    }
}

