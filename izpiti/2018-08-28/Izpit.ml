let razlika_kvadratov n m = (n+m)*(n+m) - n*n - m*m

let uporabi_na_paru f (a, b) = (f a, f b)

let rec ponovi_seznam n sez =
    if n <= 0 then []
    else sez @ (ponovi_seznam (n-1) sez)

let razdeli sez =
    let rec razdeli' n p sez = match sez with
        | [] -> n, p
        | x : xs when x >= 0 -> razdeli' n (x:p) xs
        | x : xs when x < 0 -> razdeli' (x:n) p xs
    in
    razdeli' [] [] sez

(* Če rabi bit v pravem zaporedju, uporabi List.rev *)

(* let funkcija (a,b) = [a;b]  to je neko razpakiranje elementov *)

type 'a drevo =
    | Node of ('a drevo * 'a * 'a drevo)
    | Empty


let longer_list sez1 sez2 =
    if List.length(sez1) < List.length(sez2) then sez2 else sez1 (*HACK*)

let rec padajoca max = function
    | Empty -> []
    | Node(l, x, r) ->
        if x >= max then []
        else x :: (longer_list (padajoca x l) (padajoca x r))

let rec narascajoca min = ()

let rec monotona_pot drevo = function
        | Empty -> []
        | Node(l, x, r) ->
            let left = monotona_pot l in
            let right = monotona_pot r in

            longer_list left right

(*padajoca levo, narascajoca desno ali obratno *)
(*če ne morem, ne morem, če pa loh, ga vzamem in se podaljšam*)



type 'a veriga = | Filter of ('a -> bool) * 'a list * 'a veriga
                 | Ostalo of 'a list


test = Filter((fun x = x < 0), [], Filter((fun x = x < 10), [], Ostalo([])))

let rec vstavi x veriga = function
    | Ostalo(sez) -> Ostalo(x::sez)
    | Filter(f, sez, rep) -> if f x then Filter(f, x :: sez, rep) else vstavi x rep

let rec poisci x veriga = function
    | Ostalo(sez) -> mem x sez
    | Filter(f, sez, rep) -> if f x then mem x sez else poisci x rep

let izprazni_filtre veriga =
    let rec izprazni_filtre acc veriga =
        | Ostalo(sez) -> Ostalo([]), sez @ acc
        | Filter(f, sez, rep) ->
            let (v, s) = izprazni_filtre sez @ acc rep in                        
            Filter(f, [], v), s
    in
    izprazni_filtre [] veriga

let dodaj_filter f veriga = function
    (*izprazni in po vrsti vstavljaj *)



