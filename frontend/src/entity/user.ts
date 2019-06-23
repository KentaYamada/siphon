/**
 * User entity
 */
export interface User {
    id: number | null;
    name: string;
    nickname: string;
    email: string;
    password: string;
}

/**
 * User search option entity
 */
export interface UserSearchOption {
    q: string
}
