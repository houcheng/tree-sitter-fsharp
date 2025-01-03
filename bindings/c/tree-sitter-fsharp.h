#ifndef TREE_SITTER_FSHARP_H_
#define TREE_SITTER_FSHARP_H_

typedef struct TSLanguage TSLanguage;

#ifdef __cplusplus
extern "C" {
#endif

const TSLanguage *tree_sitter_fsharp(void);
const TSLanguage *tree_sitter_fsharp_signature(void);

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_FSHARP_H_
