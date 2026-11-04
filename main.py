# Smart Grid (8 subestações, 13 ramais) — resolução com NetworkX
import sys
import networkx as nx

# ---------- Etapa 1: parametrização pelo RA ----------
RA = sys.argv[1] if len(sys.argv) > 1 else "510230"
D1, D2, D3, D4, D5, D6 = (int(c) for c in RA)
ORIGEM = "S0"
DESTINO = "S7" if D6 % 2 == 0 else "S6"     # paridade de D6

vias = [                                    # (u, v, distância em km)
    ("S0", "S1", 10 + D6 % 5), ("S0", "S2", 15 + D5 % 7),
    ("S1", "S2", 8 + D4 % 4), ("S1", "S3", 12 + D3 % 6),
    ("S2", "S4", 14 + D2 % 5), ("S2", "S5", 9 + D1 % 6),
    ("S3", "S4", 7 + (D5 + D6) % 5), ("S3", "S6", 11 + (D4 + D5) % 6),
    ("S4", "S5", 6 + (D3 + D4) % 4), ("S4", "S7", 16 + (D2 + D3) % 7),
    ("S5", "S7", 18 + (D1 + D2) % 8), ("S6", "S7", 9 + (D5 + D1) % 5),
    ("S1", "S4", 20 + D6 % 4),
]

G = nx.Graph()                              # não orientado: ida = volta
G.add_nodes_from([f"S{i}" for i in range(8)])   # garante a ordem S0..S7
G.add_weighted_edges_from(vias)
assert all(w > 0 for *_, w in G.edges(data="weight")), "Dijkstra exige pesos > 0"

M = nx.to_numpy_array(G, nodelist=list(G), weight="weight", nonedge=float("nan"))
print(f"RA: {RA} | Origem: {ORIGEM} | Destino: {DESTINO}")
print("\nMatriz de pesos (— = NULO):")
print("     " + " ".join(f"{n:>4}" for n in G))
for n, linha in zip(G, M):
    print(f"{n:>4} " + " ".join("   —" if x != x else f"{int(x):>4}" for x in linha))
print("Simétrica?", (M[~(M != M)] == M.T[~(M != M)]).all())

custo, rota = nx.single_source_dijkstra(G, ORIGEM, DESTINO, weight="weight")
ant, dist = nx.dijkstra_predecessor_and_distance(G, ORIGEM, weight="weight")
ordem = sorted(G, key=lambda n: (dist[n], int(n[1:])))
empates = list(nx.all_shortest_paths(G, ORIGEM, DESTINO, weight="weight"))
print(f"\nQ1  {ORIGEM} -> {DESTINO}: {custo} km | rota: {' -> '.join(rota)}")
print("    ordem de fechamento:", " -> ".join(ordem))
print("    distâncias L:", {n: dist[n] for n in G})
print("    antecessores:", {n: ant[n] for n in G if ant[n]})
if len(empates) > 1:
    print("    ATENÇÃO: rotas empatadas:", empates)

H = G.copy()                                # cópia: G continua completo para o Prim
H.remove_edge("S2", "S4")
custo2, rota2 = nx.single_source_dijkstra(H, ORIGEM, DESTINO, weight="weight")
print(f"\nQ2  sem e5 (S2, S4): {custo2} km | rota: {' -> '.join(rota2)}")
print(f"    acréscimo: +{custo2 - custo} km ({100 * (custo2 - custo) / custo:+.1f}%)")

T = nx.minimum_spanning_tree(G, algorithm="prim", weight="weight")
print(f"\nQ3  MST (Prim): {T.size(weight='weight'):.0f} km | ramos: {sorted(T.edges(data='weight'))}")
print(f"    soma das distâncias de Dijkstra a partir de {ORIGEM}: {sum(dist.values())} km")
