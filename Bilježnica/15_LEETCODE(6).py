Leetcode – preporučeni zadaci za vježbu
▪ Osnovno obilaženje (rekurzija na stablu)
 226. Invert Binary Tree — Easy, zamijeni lijevo/desno dijete pa rekurziraj
 938. Range Sum of BST — Easy, rekurzivno zbrajanje vrijednosti unutar raspona [low, high] BST
svojstvo dopušta da preskočimo cijela podstabla izvan raspona → ne moramo obići svaki čvor
▪ BST svojstva na djelu
 230. Kth Smallest Element in a BST — Medium, in-order obilazak daje sortirani redoslijed
 98. Validate Binary Search Tree — Medium, provjera invarijante provlačenjem granica (min,
max) kroz rekurziju
▪ Obratite pozornost na zadatak 98. koji pokazuje da lokalna provjera (samo roditelj vs.
neposredno dijete) nije dovoljna — invarijantu treba provući kroz cijelu rekurziju u obliku
gornje i donje granice.
