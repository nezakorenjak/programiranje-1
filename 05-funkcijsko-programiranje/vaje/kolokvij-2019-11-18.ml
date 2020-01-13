(* =================== *)
(* 1. naloga: funkcije *)
(* =================== *)

let is_root x y =
    if y == x * x then true else false

let pack3 x y z = (x, y, z)

let sum_if_not p list =
    let rec sum_if_not' acc p = function
        | [] -> acc
        | x :: xs -> if p x then sum_if_not' acc p xs else sum_if_not' (acc + x) p xs
        in sum_if_not' 0 p list 

let apply () = failwith "dopolni me"

(* ======================================= *)
(* 2. naloga: podatkovni tipi in rekurzija *)
(* ======================================= *)

type vrsta_srecanja = Predavanja | Vaje

type srecanje = {predmet: string; vrsta: vrsta_srecanja; trajanje: int}

type urnik = (srecanje list) list


let vaje = {predmet = "Analiza 2a"; vrsta = Vaje; trajanje = 3}
let predavanje = {predmet = "Programiranje 1"; vrsta = Predavanja; trajanje = 2}

let urnik_profesor = [[{predmet = "Analiza"; vrsta = Vaje; trajanje = 2}];[];[{predmet = "Algebra"; vrsta = Predavanja; trajanje = 1}];[];[];[{predmet = "Algebra"; vrsta = Predavanja; trajanje = 1}]]

(*poskus:*)
let rec je_preobremenjen list = match list with
    | [] -> false
    | w :: ws ->
        let rec st_vaj acc = function
            | [] -> acc
            | {vrsta = Predavanja; trajanje} :: xs -> st_vaj acc xs
            | {vrsta = Vaje; trajanje} :: xs -> st_vaj (acc + trajanje) xs in
        if st_vaj 0 w > 4 then true else je_preobremenjen ws

let bogastvo () = failwith "dopolni me"